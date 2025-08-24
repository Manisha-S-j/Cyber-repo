import requests

website = input("Enter a website URL (with http:// or https://) : ")

try:
    response = requests.get(website)
    if response.status_code == 200:

       print("website is online!")
    else:
        print("website responded with status code:",response.status_code)
except:
    print("Could not reach the website.Check the URL or your internet.")
