from PIL import Image
import torch
import transformers

# Minimal image loader
def load_image(path):
    return Image.open(path)

# Dummy preprocessing (resize + normalization)
def preprocess(img):
    return img.resize((224, 224))

# Dummy feature extractor returning a tensor
def extract_features(img):
    # Imagine this calls a pre-trained vision model
    return torch.randn(1, 512)

# Minimal LLM querying function
def query_llm(features, prompt="Describe this image"):
    # Imagine this calls an LLM with features as context
    return f"Caption for features {features.shape}"

# Pipeline chaining using pipe-like functions
def pipe(value, *funcs):
    for f in funcs:
        value = f(value)
    return value

# Minimalist one-liner chaining all together
caption = pipe(
    'sample.jpg', 
    load_image, 
    preprocess, 
    extract_features, 
    lambda x: query_llm(x, prompt="What is in the image?")
)

print(caption)  # See the magic
