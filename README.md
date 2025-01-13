# TikTok Favorite Videos Downloader 📼

This script allows users to download their favorite TikTok videos using their TikTok data JSON file and `yt-dlp`. This guide provides step-by-step instructions for setting up the script, requesting TikTok data, and customizing its behavior.

## Features

-   Parses a TikTok data JSON file to extract favorite videos.
    
-   Downloads videos into a specified folder.
    
-   Handles file name restrictions and errors gracefully.
    

----------

## Prerequisites

### Installing Python 🐍

1.  **Windows**🪟:
    
    -   Download the latest version of Python from [python.org](https://www.python.org/downloads/).
        
    -   Run the installer and check the box to add Python to your PATH during installation.
        
2.  **MacOS**🍎:
    
    -   Open Terminal and run:
        
        ```
        brew install python
        ```
        
    -   Alternatively, download the installer from [python.org](https://www.python.org/downloads/).
        
3.  **Linux**🐧:
    
    -   Use your package manager:
        
        ```
        sudo apt update
        sudo apt install python3 python3-pip
        ```
        

### Installing Required Libraries

The script requires the `yt-dlp` library. To install it:

```
pip install yt-dlp
```

----------

## How to Request TikTok Data in JSON Format 💾

1.  Open the TikTok app on your mobile device.
    
2.  Go to **Settings and Privacy**.
    
3.  Navigate to **Privacy** > **Download your data**.
    
4.  Select the JSON format and submit your request.
    
5.  Wait for TikTok to process your request. Once ready, download the file to your computer and extract it.
    
    -   Ensure the JSON file is named `tiktok_data.json` or adjust the script accordingly (see below).
        

----------

## Using the Script 📖

### Step 1: Prepare the Script

Save the script as `script.py` in your working directory.

### Step 2: Place Your Data File

-   Copy your TikTok JSON file (e.g., `tiktok_data.json`) to the same directory as `script.py`.
    

### Step 3: Customize the Script

-   **Change Output Folder**: By default, videos will be downloaded to `/mnt/d/TikTok Vids`. Edit the `download_folder` variable in the script if needed:
    
    ```
    download_folder = "<your desired folder path>"
    ```
    
    -   Windows example: `C:\Users\<YourName>\Videos\TikTok`
        
    -   MacOS/Linux example: `/Users/<YourName>/Videos/TikTok`
        
-   **Change JSON File Name**: If your JSON file has a different name, update this line:
    
    ```
    with open('tiktok_data.json', 'r', encoding='utf-8') as file:
    ```
    
    Replace `'tiktok_data.json'` with your file name.
    

### Step 4: Run the Script

1.  Open a terminal or command prompt.
    
2.  Navigate to the folder containing `script.py`:
    
    ```
    cd <path-to-your-folder>
    ```
    
3.  Run the script:
    
    ```
    python script.py
    ```
    

----------

## Troubleshooting 🛠️

### File Name Too Long Errors

-   The script limits file names to 60 characters to avoid errors. You can adjust this by editing the `outtmpl` setting:
    
    ```
    "outtmpl": os.path.join(download_folder, "%(title).60B.%(ext)s")
    ```
    
    Change `60` to a desired length.
    

### Missing Libraries

-   Ensure `yt-dlp` is installed:
    
    ```
    pip install yt-dlp
    ```
    

### Permission Denied Errors

-   Ensure you have write permissions for the download folder. Use an accessible directory or adjust permissions.
    

### JSON Parsing Errors

-   Verify your TikTok data file is complete and not corrupted.
    

----------

## Additional Notes

-   For large download batches, consider using a fast and stable internet connection.
    
-   This script does not support videos that are unavailable or deleted from TikTok.
    

----------

## Disclaimer

This script is for personal use only. Ensure you comply with TikTok’s terms of service when using this tool.
