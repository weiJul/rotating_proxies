import queue
import threading
import requests

# Initialize a queue to hold the proxies
q = queue.Queue()
# List to store valid HTTP proxies
valid_proxies = []

# Load proxies from file into the queue
with open("data/http_proxies.txt") as f:
    proxies = f.read().strip().split("\n")
    for proxy in proxies:
        q.put(proxy)

def check_proxies():
    """
    Function to check if proxies are valid by attempting a request to ipinfo.io.
    Valid proxies are added to the valid_http_proxies list.
    """
    global q
    while not q.empty():
        proxy = q.get()
        try:
            response = requests.get('http://ipinfo.io/json', proxies={'http': proxy, 'https': proxy}, timeout=5)
            if response.status_code == 200:
                valid_proxies.append(proxy)
                print(f"Valid proxy found: {proxy}")
        except requests.RequestException:
            # Ignore failed requests
            continue

# Start multiple threads to speed up the proxy validation process
threads = []
for _ in range(5):
    thread = threading.Thread(target=check_proxies)
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()

# # Store valid proxies if needed:
# # Write valid proxies to a file
# with open("data/valid_http_proxies.txt", "w") as f:
#     for proxy in valid_proxies:
#         f.write(proxy + "\n")
#
# # Reload the valid proxies for further usage
# with open("data/valid_http_proxies.txt", "r") as f:
#     valid_proxies = f.read().strip().split("\n")

# List of websites to scrape
websites = ["http:// example website .com"]

# Loop over websites and use each proxy to send a request
for idx, site in enumerate(websites):
    if idx < len(valid_proxies):
        proxy = valid_proxies[idx]
        try:
            print(f"Using proxy: {proxy}")
            response = requests.get(site, proxies={"http": proxy, "https": proxy}, timeout=5)
            print(f"Status Code: {response.status_code}")
            print(response.text)
        except requests.RequestException:
            print("Request failed with proxy:", proxy)
    else:
        print("Not enough valid proxies to continue scraping.")
        break
