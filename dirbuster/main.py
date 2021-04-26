import requests


def request(url):
    try:
        return requests.get(f"http://{url}")
    except requests.exceptions.ConnectionError:
        pass


target_url = input("[*] Enter Target URL: ")

file = open("big.txt", "r")

for line in file:
    word = line.strip()
    full_url = target_url + "/" + word
    response = request(full_url)
    if response:
        print(f"[+] Discovered Directory At This Link: {full_url}")

