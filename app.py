import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"]='1'
from huggingface_hub import snapshot_download
from transformers import pipeline

class InferlessPythonModel:
    def initialize(self):
        snapshot_download(repo_id="vasista22/whisper-hindi-large-v2",allow_patterns=["*.safetensors"])
        self.generator = pipeline("automatic-speech-recognition", model="vasista22/whisper-hindi-large-v2",device=0)

    def infer(self, inputs):
        audio_url =  inputs["audio_url"]
        
        pipeline_output = self.generator(audio_url)
        generated_txt = pipeline_output["text"]
        data = { "transcribed_text" : generated_txt } 
        return data

    def finalize(self):
        self.pipe = None
