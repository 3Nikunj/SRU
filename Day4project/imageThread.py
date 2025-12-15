import requests
import time
import os
import threading
import concurrent.futures

DOWNDLOAD_DIR = "downloaded_images"
if not os.path.exists(DOWNDLOAD_DIR):
    os.makedirs(DOWNDLOAD_DIR)


def download_image(image_url):
    img_id = image_url.split("/")[4]
    filename = DOWNDLOAD_DIR + "/" + img_id + ".jpg"
    print("thread:", threading.get_ident(), "Starting download:", filename)

    try:
        response = requests.get(image_url)

        if response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(response.content)
            print("thread:", threading.get_ident(),
                  "Finished download:", filename)
        else:
            print("thread:", threading.get_ident(),
                  "Failed to download:", filename)
    except Exception as e:
        print("thread:", threading.get_ident(),
              "Error downloading", filename, ":", e)


img_urls = []
for i in range(10, 20):   # 10 20
    img_urls.append("https://picsum.photos/id/"+str(i)+"/200/300")


def running_threads():
    start_time = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_image, img_urls)
    end_time = time.perf_counter()
    print("Total time with threads:", end_time - start_time)


running_threads()
