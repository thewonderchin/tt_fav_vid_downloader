import json
import os
from yt_dlp import YoutubeDL

def main():
    with open('tiktok_data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    favorite_videos = data["Activity"]["Favorite Videos"]["FavoriteVideoList"]

    download_folder = "/mnt/d/TikTok Vids"
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    # Example: shorten the title to 60 chars to avoid "File name too long" errors
    ydl_opts = {
        "outtmpl": os.path.join(download_folder, "%(title).60B.%(ext)s"),
        "restrictfilenames": True,  # Keep filenames simple (ASCII only)
    }

    with YoutubeDL(ydl_opts) as ydl:
        for item in favorite_videos:
            link = item["Link"]
            print(f"Attempting to download: {link}")
            try:
                ydl.download([link])
            except Exception as e:
                print(f"  ► Skipping due to error: {e}")
                # continue to the next link
                continue

if __name__ == "__main__":
    main()
