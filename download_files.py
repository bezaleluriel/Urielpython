from threading import Thread

import requests
import time

def download_file(url):
    link = url.replace("'", "").strip()
    response = requests.get(link)
    with open(url.strip().split("/")[-1] + '.jpg2', "wb") as outfile:
        outfile.write(response.content)

file_path = r'Z:\___advanced python\list_of_images.txt'
with open(file_path, "r") as file:
    urls = file.readlines()

# regular case
start_time = time.time()
for url in urls:
    link = url.replace("'", "").strip()
    response = requests.get(link)
    with open(url.strip().split("/")[-1] + '.jpg', "wb") as outfile:
        outfile.write(response.content)
end_time = time.time()
elapsed_time = end_time - start_time
print("Elapsed time regular case:", elapsed_time, "seconds")

# with threads
start_time2 = time.time()
threads = []
for url in urls:
    thread = Thread(target= download_file,args=(url,) )
    # remember not forget this!!
    threads.append(thread)
    thread.start()
# the join is after the loop so the thread will be effective and work in parallel
for thread in threads:
    thread.join()

end_time2 = time.time()
elapsed_time2 = end_time2 - start_time2
print("Elapsed time2 regular case:", elapsed_time2, "seconds")
