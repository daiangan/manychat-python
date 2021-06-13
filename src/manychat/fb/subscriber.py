from dataclasses import dataclass

from ..utils import api


@dataclass
class Subscriber(api.API):
    api_key: str
    base_endpoint = 'subscriber'

    def get_info(self, subscriber_id: str) -> dict:
        params = {
            'subscriber_id': subscriber_id,
        }

        response = self.api_request(
            method='GET',
            endpoint=f'{self.base_endpoint}/getInfo',
            params=params,
        )

        return response
