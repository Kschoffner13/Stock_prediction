import kagglehub
import shutil
import os

# Download latest version
path = kagglehub.dataset_download("jacksoncrow/stock-market-dataset")

print("Path to dataset files:", path)

# Define your target directory
target_dir = r"c:\PROJECTS\Stock_prediction\data\archive"

# Create target directory if it doesn't exist
os.makedirs(target_dir, exist_ok=True)

# Copy all files from downloaded path to target directory
for item in os.listdir(path):
    src = os.path.join(path, item)
    dst = os.path.join(target_dir, item)
    
    if os.path.isfile(src):
        shutil.copy2(src, dst)
        print(f"Copied: {item}")
    elif os.path.isdir(src):
        shutil.copytree(src, dst, dirs_exist_ok=True)
        print(f"Copied directory: {item}")

print(f"\nAll files saved to: {target_dir}")