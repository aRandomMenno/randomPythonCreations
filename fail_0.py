
import os

# Specify the directory where the files are located
directory_path = r'C:\Users\menno\AppData\Roaming\ATLauncher\instances\MCLATESTFBR\songs'  # Change this to your actual directory path

# Iterate over all files in the directory
for filename in os.listdir(directory_path):
    # Check if the filename contains '-'
    if '–' in filename:
        # Replace '–' with '_'
        new_filename = filename.replace('–', '_')
        # Construct the full path of the original and new filenames
        old_file_path = os.path.join(directory_path, filename)
        new_file_path = os.path.join(directory_path, new_filename)
        # Rename the file
        os.rename(old_file_path, new_file_path)

print("All files renamed successfully.")
