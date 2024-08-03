# Google Drive Batch Delete

This repository contains a script to batch delete all files and folders from a Google Drive folder that match a specific pattern using Google Colab and PyDrive2. This allows you to manage your Google Drive files directly in your browser.

## Features

- **No Coding Skills Required**: You don't need to know any programming or coding to use this script.
- **Browser-Based Solution**: All steps are performed online in your web browser using Google Colab.
- **Simple and Easy Setup**: Follow the step-by-step instructions to quickly set up and run the script.
- **Automated Process**: The script automates the deletion process, saving you time and effort.
- **User-Friendly Instructions**: Detailed, user-friendly instructions make it easy for anyone to follow.

## Prerequisites

- A Google account with access to Google Drive.

## Setup Instructions

### Step 1: Obtain Folder ID

1. **Root Folder ID**:
   - Open the folder in Google Drive.
   - The URL will look something like this: `https://drive.google.com/drive/folders/ROOT_FOLDER_ID`.
   - Copy the `ROOT_FOLDER_ID` from the URL.

### Step 2: Check Permissions

- Ensure you have write access to the folder and its subfolders.

### Step 3: Run the Script

1. Open [Google Colab](https://colab.research.google.com/) and create a new notebook.
2. Copy the contents of `batch_delete_drive_files.py` into a cell in the notebook.
3. Replace `ROOT_FOLDER_ID` and `pattern` with the ID obtained in Step 1 and the pattern you want to match.
4. **Grant Permissions**: When prompted, a pop-up window will ask for permissions to access your Google Drive. Make sure to tick all the necessary boxes to grant permissions.
5. Run the cell to execute the script.

## Time Estimates

- **Obtain Folder ID**: 2-5 minutes
- **Check Permissions**: 2-5 minutes
- **Run the Script**: 10-30 minutes (depending on the size of the folder and internet speed)

## Script

The script is located in the file `batch_delete_drive_files.py`.

### Usage

1. **Copy**: Copy the script into a new cell in a Google Colab notebook.
2. **Edit**: Replace the placeholder folder ID and pattern with your actual folder ID and the pattern you want to match.
3. **Execute**: Run the cell to start deleting files and folders.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Related Projects

- [Google Drive Folder Copy](https://github.com/similato87/google-drive-folder-copy): Use your browser to copy files from others' shared Google Drive folders to your own Google Drive, all online in the browser.

## Key Topics

- no coding required
- browser-based solution
- easy setup
- quick execution
- automated process
- secure
- user-friendly instructions
- error handling
- time-efficient
- online
- Google Drive
- Google Colab
- PyDrive2
- file deletion
- recursive deletion
