from urllib.error import HTTPError
import urllib.request
import requests

from config import IPFS_HOST


def load_from_ipfs(ipfs_hash: str, ipfs_service: str = 'https://ipfs.io/ipfs/'):
    try:
        with urllib.request.urlopen(ipfs_service+ipfs_hash) as _url:
            return _url.read().decode()
    except HTTPError:
        print('url is not accessible')
    return None


def upload_text(text: str, print_message: bool = True):
    if print_message:
        print(f'Uploading text: {text}')
    try:
        files = {
            'file': ('text', text)
        }
        response = requests.post(f'{IPFS_HOST}/api/v0/add', files=files)
        return response.json()['Hash'], None
    except Exception as upload_error:
        print(upload_error)
        return None, upload_error


def upload_file(file_name: str):
    print(f'Uploading file: {file_name}')
    try:
        files = {
            'file': ('file_name', open(file_name, 'rb'))
        }
        response = requests.post(f'{IPFS_HOST}/api/v0/add', files=files)
        return response.json()['Hash'], None
    except Exception as upload_error:
        print(upload_error)
        return None, upload_error
