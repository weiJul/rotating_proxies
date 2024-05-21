# Rotating Proxies

This repository contains a Python script to validate a list of HTTP proxies and use them to send requests to websites. The script employs multi-threading to speed up the validation process.
## Features

    Proxy Validation: Checks if proxies are valid by attempting to send a request to ipinfo.io.
    Multi-threading: Uses 50 threads to speed up the validation process.
    Proxy Usage: Utilizes the valid proxies to send requests to a list of websites.


## Usage
    Prepare your proxy list: Add your HTTP proxies to the file data/http_proxies.txt.
    Run the script: Execute the script to validate proxies and use them for making requests.


##  rotating_proxies.py
    Output: The script will print valid proxies and their status when used for requests.

## Script Details
    Initialize Threads: The script initializes 50 threads to validate proxies.
    Validate Proxies: Each thread picks a proxy from the queue and tries to send a request to http://ipinfo.io/json. Valid proxies are stored in the valid_proxies list.
    Use Valid Proxies: The script loops over a list of websites and uses the validated proxies to send requests.

## Example Proxy List

### Your data/http_proxies.txt should look like this:

  http://proxy1:port
  
  http://proxy2:port
  
  ...

### Example Website List
Modify the websites list in the script to include the websites you want to scrape:

websites = ["http:// example website .com"]
