import json
from dataclasses import dataclass, field

import requests


@dataclass
class ManyChatAPI:
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

        try:
            mc_response = None

            if method == 'GET':
                mc_response = requests.get(
                    url=f'{self.api_base_url}{endpoint}',
                    headers=self.headers,
                    params=params,
                    timeout=5,
                )

            elif method == 'POST':
                mc_response = requests.post(
                    url=f'{self.api_base_url}{endpoint}',
                    headers=self.headers,
                    data=json.dumps(params),
                    timeout=5,
                )

            else:
                return NotImplemented

        except Exception as e:
            response = {
                'status': 'error',
                'message': e,
            }

        else:
            response = json.loads(mc_response.text)

        return response
