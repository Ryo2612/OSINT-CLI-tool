import requests 

def get_http_info(domain):
	response = requests.get(f"https://{domain}")
	print(response.status_code)
