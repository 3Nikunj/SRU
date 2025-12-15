import threading
import requests
import time
import os
import concurrent.futures

# 1. Setup specific download folder
DOWNLOAD_DIR = 'downloads'
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)


def download_image(img_url):
    """
    Downloads a single image from the web and saves it to disk.
    """
    # Extract a filename from the URL (or make one up)
    # URLs look like: https://picsum.photos/id/10/800/800
    img_id = img_url.split('/')[4]
    filename = f"{DOWNLOAD_DIR}/image_{img_id}.jpg"

    print(f"⬇️  Thread {threading.get_ident()}: Starting {filename}...")

    try:
        # REAL network request
        response = requests.get(img_url)

        # Check if the download was successful (Status Code 200)
        if response.status_code == 200:
            # Write the binary content to a file
            with open(filename, 'wb') as f: 
                f.write(response.content)
            print(f"✅  Saved {filename}")
        else:
            print(f"❌  Failed to retrieve {img_url}")

    except Exception as e:
        print(f"⚠️  Error downloading {img_url}: {e}")


# List of 10 real image URLs (Picsum provides free placeholders)
img_urls = [
    f"https://picsum.photos/id/{i}/1600/900" for i in range(10, 20)
]


def run_threaded_download():
    start_time = time.perf_counter()

    # We use a context manager to handle the threads automatically
    # max_workers=5 means we download 5 images at the exact same time
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_image, img_urls)

    end_time = time.perf_counter()
    print(
        f"\n--- 🚀 Done! Downloaded {len(img_urls)} images in {round(end_time - start_time, 2)} seconds ---")


if __name__ == "__main__":
    print(f"Starting download of {len(img_urls)} high-res images...")
    run_threaded_download()
