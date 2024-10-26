import requests
import torch
from PIL import Image
from transformers import MllamaForConditionalGeneration, AutoProcessor
from huggingface_hub import login
from accelerate import dispatch_model

# Authenticate with Hugging Face
login(token="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")

model_id = "meta-llama/Llama-3.2-11B-Vision-Instruct"

# Load the model with offloading
model = MllamaForConditionalGeneration.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    offload_folder="offload",  # Specify a folder for offloading
)

# Dispatch the model to handle offloading
dispatch_model(model, offload_folder="offload")

processor = AutoProcessor.from_pretrained(model_id)

url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/0052a70beed5bf71b92610a43a52df6d286cd5f3/diffusers/rabbit.jpg"
image = Image.open(requests.get(url, stream=True).raw)

messages = [
    {"role": "user", "content": [
        {"type": "image", "url": r"C:\Users\samsu\Pictures\Screenshots\end of 2018.png"},
        {"type": "text"}
    ]}
]
input_text = processor.apply_chat_template(messages, add_generation_prompt=True)
inputs = processor(
    image,
    input_text,
    add_special_tokens=False,
    return_tensors="pt"
)

output = model.generate(**inputs, max_new_tokens=30)
print(processor.decode(output[0]))
