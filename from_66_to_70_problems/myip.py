import json
import requests


def get_external_ip():
    try:
        response = requests.get('http://httpbin.org/get')
        data = response.json()
        print('data from response json', data)
        ip_address = data['origin']
        return ip_address
    except Exception as e:
        print(f"An error occured: {e}")
        return None


if __name__ == "__main__":
    ip_address = get_external_ip()
    if ip_address:
        print(ip_address)