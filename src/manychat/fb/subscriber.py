from dataclasses import dataclass

from ..utils import api


@dataclass
class Subscriber(api.API):
    api_key: str
    base_endpoint = 'subscriber'

    def get_info(self, subscriber_id: str) -> dict:
        response = self.api_request(
            method='GET',
            endpoint=f'{self.base_endpoint}/getInfo',
            params={
                'subscriber_id': subscriber_id,
            },
        )
        return response

    def find_by_name(self, name: str) -> dict:
        response = self.api_request(
            method='GET',
            endpoint=f'{self.base_endpoint}/findByName',
            params={
                'name': name,
            },
        )
        return response

    def get_info_by_user_ref(self, user_ref: int) -> dict:
        response = self.api_request(
            method='GET',
            endpoint=f'{self.base_endpoint}/getInfoByUserRef',
            params={
                'user_ref': user_ref,
            },
        )
        return response

    def find_by_custom_field(self,
                             field_id: int,
                             field_value: str) -> dict:
        response = self.api_request(
            method='GET',
            endpoint=f'{self.base_endpoint}/findByCustomField',
            params={
                'field_id': field_id,
                'field_value': field_value,
            },
        )
        return response

    def find_by_system_field(self,
                             email: str,
                             phone:str) -> dict:
        response = self.api_request(
            method='GET',
            endpoint=f'{self.base_endpoint}/findBySystemField',
            params={
                'email': email,
                'phone': phone,
            },
        )
        return response

    def add_tag(self,
                subscriber_id: int,
                tag_id: int) -> dict:
        response = self.api_request(
            method='POST',
            endpoint=f'{self.base_endpoint}/addTag',
            params={
                'subscriber_id': subscriber_id,
                'tag_id': tag_id,
            },
        )
        return response

    def add_tag_by_name(self,
                        subscriber_id: int,
                        tag_name: str) -> dict:
        response = self.api_request(
            method='POST',
            endpoint=f'{self.base_endpoint}/addTagByName',
            params={
                'subscriber_id': subscriber_id,
                'tag_name': tag_name,
            },
        )
        return response

    def remove_tag(self,
                   subscriber_id: int,
                   tag_id: int) -> dict:
        response = self.api_request(
            method='POST',
            endpoint=f'{self.base_endpoint}/removeTag',
            params={
                'subscriber_id': subscriber_id,
                'tag_id': tag_id,
            },
        )
        return response

    def remove_tag_by_name(self,
                           subscriber_id: int,
                           tag_name: str) -> dict:
        response = self.api_request(
            method='POST',
            endpoint=f'{self.base_endpoint}/removeTagByName',
            params={
                'subscriber_id': subscriber_id,
                'tag_name': tag_name,
            },
        )
        return response

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

