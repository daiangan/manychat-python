import json
from dataclasses import dataclass, field

import requests


@dataclass
class API:
    api_base_url = 'https://api.manychat.com/fb/'
    api_key: str
    headers: dict = field(init=False)

    def __post_init__(self):
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}',
        }

    def api_request(self,
                    method: str,
                    endpoint: str,
                    params: dict,
                    ):

        response = {
            'status': 'success',
            'message': 'Everything ok.',
            'data': None,
        }

        if method == 'GET':
            try:
                mc_response = requests.get(
                    url=f'{self.api_base_url}{endpoint}',
                    headers=self.headers,
                    params=params,
                    timeout=5,
                )
            except Exception as e:
                response = {
                    'status': 'error',
                    'message': e,
                }
            else:
                response = json.loads(mc_response.text)

        return response
