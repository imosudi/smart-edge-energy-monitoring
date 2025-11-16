from infer import InferenceEngine
import numpy as np

def test_infer_runs():
    ie = InferenceEngine(model_path='/app/models/dummy.tflite')
    waveform = (np.sin(2*np.pi*0.1*np.arange(128))).tolist()
    preds, lat = ie.infer_nilm(waveform)
    assert isinstance(preds, dict)
    assert lat >= 0
