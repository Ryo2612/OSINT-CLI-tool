import requests
import os

from dotenv import load_dotenv

load_dotenv()

def get_ip_info(ip_address):
	token = os.getenv("IPINFO_TOKEN")
	url = f"https://api.ipinfo.io/lite/{ip_address}?token={token}"
	response = requests.get(url)
	if response.status_code != 200:
		return None
	return response.json()
