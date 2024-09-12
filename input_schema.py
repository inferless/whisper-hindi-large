INPUT_SCHEMA = {
    "audio_url": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["https://cdn-media.huggingface.co/speech_samples/sample2.flac"]
    },
    "language": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["hi"]
    },
    "task": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["transcribe"]
    },
    "return_timestamps": {
        'datatype': 'BOOL',
        'required': True,
        'shape': [1],
        'example': [True]
    }
}
