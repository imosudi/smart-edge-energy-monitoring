#include <WiFi.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>

const char* ssid = "YOUR_SSID";
const char* password = "YOUR_PASS";
const char* mqtt_server = "192.168.1.50"; // edge gateway or broker

WiFiClient espClient;
PubSubClient client(espClient);

String device_id = "esp32-001";
String house_id = "home-01";

void setup_wifi() {
  delay(10);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) { delay(500); }
}

void reconnect() {
  while (!client.connected()) {
    if (client.connect(device_id.c_str())) {
      // connected
    } else {
      delay(2000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
}

void loop() {
  if (!client.connected()) reconnect();
  client.loop();

  // simulate telemetry
  StaticJsonDocument<512> doc;
  doc["ts"] = "2025-11-16T05:00:00.000Z";
  doc["device_id"] = device_id;
  doc["house_id"] = house_id;
  doc["v"] = 230.2;
  doc["i"] = 0.48;
  JsonArray samples = doc.createNestedArray("ct_sample");
  for (int i=0; i<128; i++) {
    samples.add(sin(i * 0.1));
  }
  char buffer[512];
  serializeJson(doc, buffer);
  String topic = "home/" + house_id + "/device/" + device_id + "/telemetry";
  client.publish(topic.c_str(), buffer);
  delay(1000);
}
