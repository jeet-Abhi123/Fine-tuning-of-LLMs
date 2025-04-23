from datasets import load_dataset
from PIL import Image


# Define a custom data loading function
def data_loader(example):
    image_path = f"{data_dir}/{example['Image_path']}"
    example['image'] = Image.open(image_path).convert("RGB")
    return example


data_dir = r"C:\Users\abhij\Desktop\Projects\Research Work\finetuing basics\PaliGemma_VLM\data"

# Load dataset and map image data
dataset = load_dataset(
    "csv",
    data_files=f"{data_dir}/dataset.csv"
).map(data_loader, remove_columns=['Image_path'])

# Reorder columns to have 'image' first
dataset = dataset.map(lambda x: {
    'image': x['image'],
    'Question': x['Question'],
    'Answer': x['Answer']
})

# Push dataset to Hugging Face Hub
dataset.push_to_hub("Kaith-jeet123/brain_tumor_vqa")
