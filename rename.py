import os

def change_dataset_filename():
  # Path to your folder containing images
  folder_path = 'dataset'

  # List all images in the folder
  all_images = [img for img in os.listdir(folder_path) if img.lower(
  ).endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif'))]

  # Sort the images to maintain a consistent order
  all_images.sort()

  # Rename images
  for idx, image in enumerate(all_images, start=1):
    old_path = os.path.join(folder_path, image)
    extension = os.path.splitext(image)[1]  # Get the file extension
    new_name = f'id_{idx}{extension}'
    new_path = os.path.join(folder_path, new_name)
    try:
      os.rename(old_path, new_path)
      print(f'Renamed: {old_path} -> {new_path}')
    except Exception as e:
      print(f"Error renaming {old_path}: {e}")

  print("All images have been renamed successfully.")


if __name__ == '__main__':
  change_dataset_filename()
