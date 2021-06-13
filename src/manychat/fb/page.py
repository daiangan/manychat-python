from dataclasses import dataclass

from ..utils import api


@dataclass
class Page(api.API):
    api_key: str
    base_endpoint = 'page'

    def get_info(self) -> dict:
        response = self.api_request(
            method='GET',
            endpoint=f'{self.base_endpoint}/getInfo',
            params={},
        )

        return response
