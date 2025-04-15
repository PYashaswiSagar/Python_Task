import os
import requests
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from typing import List

# Replace with your own API key from https://api.nasa.gov
API_KEY = "DEMO_KEY"  # Replace with your own key!
APOD_ENDPOINT = 'https://api.nasa.gov/planetary/apod'
OUTPUT_IMAGES = './output2'


def get_apod_metadata(start_date: str, end_date: str, api_key: str) -> List[dict]:
    """
    Fetch metadata from NASA APOD API between two dates.
    """
    params = {
        'api_key': api_key,
        'start_date': start_date,
        'end_date': end_date
    }

    response = requests.get(APOD_ENDPOINT, params=params)
    response.raise_for_status()  # Raise error if the request failed

    metadata = response.json()
    return metadata


def download_image(item: dict):
    """
    Download a single image from metadata dictionary.
    """
    if item.get("media_type") != "image":
        return  # Skip videos or unsupported types

    url = item.get("url")
    date = item.get("date")
    title = item.get("title", "image")

    # Create filename like 2021-08-01-title.jpg
    ext = url.split('.')[-1]  # jpg or png
    filename = f"{date}-{title[:30].replace(' ', '_')}.{ext}"
    filepath = os.path.join(OUTPUT_IMAGES, filename)

    try:
        img_data = requests.get(url).content
        with open(filepath, 'wb') as f:
            f.write(img_data)
        print(f"✅ Downloaded: {filename}")
    except Exception as e:
        print(f" Failed to download {url}: {e}")


def download_apod_images(metadata: list):
    """
    Download all image URLs in parallel using threading.
    """
    if not os.path.exists(OUTPUT_IMAGES):
        os.makedirs(OUTPUT_IMAGES)

    # Use ThreadPoolExecutor for concurrent downloading
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(download_image, metadata)


def main():
    metadata = get_apod_metadata(
        start_date='2021-08-01',
        end_date='2021-09-30',
        api_key=API_KEY,
    )
    download_apod_images(metadata=metadata)


if __name__ == '__main__':
    main()
