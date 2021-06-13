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

    def find_by_name(self):
        return NotImplemented

    def get_info_by_user_ref(self):
        return NotImplemented

    def find_by_custom_field(self):
        return NotImplemented

    def find_by_system_field(self):
        return NotImplemented

    def add_tag(self):
        return NotImplemented

    def add_tag_by_name(self):
        return NotImplemented

    def remove_tag(self):
        return NotImplemented

    def remove_tag_by_name(self):
        return NotImplemented

    def set_custom_field(self):
        return NotImplemented

    def set_custom_fields(self):
        return NotImplemented

    def set_custom_field_by_name(self):
        return NotImplemented

    def verify_by_signed_request(self):
        return NotImplemented

    def create_subscriber(self):
        return NotImplemented

    def update_subscriber(self):
        return NotImplemented

