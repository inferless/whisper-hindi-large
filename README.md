# Whisper-Hindi-Large

Whisper is an ASR (Automatic Spech Recognition) model developed by OpenAI. This template refers to the fine-tuned version of the model on the Hindi Dataset. You can use this template to import the model on Inferless.

## TL;DR:
- Deployment of Whisper-Hindi-Large model using [Transformers](https://github.com/huggingface/transformers).
- Dependencies defined in `inferless-runtime-config.yaml`.
- GitHub/GitLab template creation with `app.py`, `inferless-runtime-config.yaml` and `inferless.yaml`.
- Model class in `app.py` with `initialize`, `infer`, and `finalize` functions.
- Custom runtime creation with necessary system and Python packages.
- Model import via GitHub with `input_schema.py` file.
- Recommended GPU: NVIDIA A100.
- Custom runtime selection in advanced configuration.
- Final review and deployment on the Inferless platform.

### Fork the Repository
Get started by forking the repository. You can do this by clicking on the fork button in the top right corner of the repository page.

This will create a copy of the repository in your own GitHub account, allowing you to make changes and customize it according to your needs.

### Create a Custom Runtime in Inferless
To access the custom runtime window in Inferless, simply navigate to the sidebar and click on the Create new Runtime button. A pop-up will appear.

Next, provide a suitable name for your custom runtime and proceed by uploading the **inferless-runtime-config.yaml** file given above. Finally, ensure you save your changes by clicking on the save button.

### Import the Model in Inferless
Log in to your inferless account, select the workspace you want the model to be imported into and click the `Add a custom model` button.

- Select `Github` as the method of upload from the Provider list and then select your Github Repository and the branch.
- Choose the type of machine, and specify the minimum and maximum number of replicas for deploying your model.
- Configure Custom Runtime ( If you have pip or apt packages), choose Volume, Secrets and set Environment variables like Inference Timeout / Container Concurrency / Scale Down Timeout
- Once you click “Continue,” click Deploy to start the model import process.

Enter all the required details to Import your model. Refer [this link](https://docs.inferless.com/integrations/git-custom-code/git--custom-code) for more information on model import.


## Curl Command
Following is an example of the curl command you can use to make inference. You can find the exact curl command in the Model's API page in Inferless.

```bash
curl --location '<your_inference_url>' \
          --header 'Content-Type: application/json' \
          --header 'Authorization: Bearer <your_api_key>' \
          --data '{
                    "inputs": [
                        {
                            "data": [
                                "https://cdn-media.huggingface.co/speech_samples/sample2.flac"
                            ],
                            "name": "audio_url",
                            "shape": [
                                1
                            ],
                            "datatype": "BYTES"
                        },
                        {
                            "data": [
                                "hi"
                            ],
                            "name": "language",
                            "shape": [
                                1
                            ],
                            "datatype": "BYTES"
                        },
                        {
                            "data": [
                                "transcribe"
                            ],
                            "name": "task",
                            "shape": [
                                1
                            ],
                            "datatype": "BYTES"
                        },
                        {
                            "data": [
                                true
                            ],
                            "name": "return_timestamps",
                            "shape": [
                                1
                            ],
                            "datatype": "BOOL"
                        }
                    ]
                }'
```

## Customizing the Code
Open the `app.py` file. This contains the main code for inference. It has three main functions, initialize, infer and finalize.

**Initialize** -  This function is executed during the cold start and is used to initialize the model. If you have any custom configurations or settings that need to be applied during the initialization, make sure to add them in this function.

**Infer** - This function is where the inference happens. The argument to this function `inputs`, is a dictionary containing all the input parameters. The keys are the same as the name given in inputs. Refer to [input](#input) for more.

```python
def infer(self, inputs):
    audio_url = inputs["audio_url"]
```

**Finalize** - This function is used to perform any cleanup activity for example you can unload the model from the gpu by setting `self.pipe = None`.


For more information refer to the [Inferless docs](https://docs.inferless.com/)
