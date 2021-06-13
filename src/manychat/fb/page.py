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

    def create_tag(self):
        return NotImplemented

    def get_tags(self):
        return NotImplemented

    def remove_tag(self):
        return NotImplemented

    def remove_tag_by_name(self):
        return NotImplemented

    def create_custom_field(self):
        return NotImplemented

    def get_growth_tools(self):
        return NotImplemented

    def get_flows(self):
        return NotImplemented

    def get_custom_fields(self):
        return NotImplemented

    def get_otn_topics(self):
        return NotImplemented

    def get_bot_fields(self):
        return NotImplemented

    def create_bot_field(self):
        return NotImplemented

    def set_bot_field(self):
        return NotImplemented

    def set_bot_field_by_name(self):
        return NotImplemented

    def set_bot_fields(self):
        return NotImplemented
