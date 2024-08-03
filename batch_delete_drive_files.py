# Install PyDrive2
!pip install pydrive2

from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

# Authenticate and create the PyDrive client.
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)

# ID of the root folder to start the deletion process (replace with the actual folder ID)
root_folder_id = 'ROOT_FOLDER_ID'  # Replace with your root folder ID

# Pattern to match filenames (e.g., "_xx")
pattern = '_xx'

# Function to list all files and folders in a given folder
def list_files_and_folders(folder_id):
    try:
        file_list = drive.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()
        return file_list
    except Exception as e:
        print(f"Failed to list files in folder with ID: {folder_id}, Error: {e}")
        return []

# Function to recursively delete files matching the pattern
def delete_files_recursively(folder_id, pattern):
    items = list_files_and_folders(folder_id)
    for item in items:
        try:
            if item['mimeType'] == 'application/vnd.google-apps.folder':
                # Recursively delete files in the subfolder
                delete_files_recursively(item['id'], pattern)
            elif pattern in item['title']:
                # Delete the file if it matches the pattern
                item.Delete()
                print(f"Deleted file: {item['title']}")
        except Exception as e:
            print(f"Failed to delete item: {item['title']}, Error: {e}")

# Start the recursive deletion process from the root folder
delete_files_recursively(root_folder_id, pattern)
