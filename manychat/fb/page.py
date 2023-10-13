from dataclasses import dataclass
from typing import Union, List

from ..api import ManyChatAPI


@dataclass
class Page(ManyChatAPI):
    api_key: str
    base_endpoint = 'page'

    def get_info(self) -> dict:
        response = self.api_request(
            method='GET',
            endpoint=f'{self.base_endpoint}/getInfo',
            params={},
        )
        return response

    def create_tag(self, name: str) -> dict:
        response = self.api_request(
            method='POST',
            endpoint=f'{self.base_endpoint}/createTag',
            params={
                'name': name,
            },
        )
        return response

    def get_tags(self) -> dict:
        response = self.api_request(
            method='GET',
            endpoint=f'{self.base_endpoint}/getTags',
            params={},
        )
        return response

    def remove_tag(self, tag_id: int) -> dict:
        response = self.api_request(
            method='POST',
            endpoint=f'{self.base_endpoint}/removeTag',
            params={
                'tag_id': tag_id,
            },
        )
        return response

    def remove_tag_by_name(self, tag_name: str) -> dict:
        response = self.api_request(
            method='POST',
            endpoint=f'{self.base_endpoint}/removeTagByName',
            params={
                'tag_name': tag_name,
            },
        )
        return response

    def create_custom_field(self,
                            caption: str,
                            field_type: str,
                            description: str) -> dict:
        response = self.api_request(
            method='POST',
            endpoint=f'{self.base_endpoint}/createCustomField',
            params={
                'caption': caption,
                'type': field_type,
                'description': description,
            },
        )
        return response

    def get_growth_tools(self) -> dict:
        response = self.api_request(
            method='GET',
            endpoint=f'{self.base_endpoint}/getGrowthTools',
            params={},
        )
        return response

    def get_flows(self) -> dict:
        response = self.api_request(
            method='GET',
            endpoint=f'{self.base_endpoint}/getFlows',
            params={},
        )
        return response

    def get_custom_fields(self) -> dict:
        response = self.api_request(
            method='GET',
            endpoint=f'{self.base_endpoint}/getCustomFields',
            params={},
        )
        return response

    def get_otn_topics(self) -> dict:
        response = self.api_request(
            method='GET',
            endpoint=f'{self.base_endpoint}/getOtnTopics',
            params={},
        )
        return response

    def get_bot_fields(self) -> dict:
        response = self.api_request(
            method='GET',
            endpoint=f'{self.base_endpoint}/getBotFields',
            params={},
        )
        return response

    def create_bot_field(self,
                         name: str,
                         field_type: str,
                         description: str,
                         value: Union[str, int, bool]) -> dict:
        response = self.api_request(
            method='POST',
            endpoint=f'{self.base_endpoint}/createBotField',
            params={
                'name': name,
                'type': field_type,
                'description': description,
                'value': value,
            },
        )
        return response

    def set_bot_field(self,
                      field_id: int,
                      field_value: Union[str, int, bool]) -> dict:
        response = self.api_request(
            method='POST',
            endpoint=f'{self.base_endpoint}/setBotField',
            params={
                'field_id': field_id,
                'field_value': field_value,
            },
        )
        return response

    def set_bot_field_by_name(self,
                              field_name: str,
                              field_value: Union[str, int, bool]) -> dict:
        response = self.api_request(
            method='POST',
            endpoint=f'{self.base_endpoint}/setBotFieldByName',
            params={
                'field_name': field_name,
                'field_value': field_value,
            },
        )
        return response

    def set_bot_fields(self, fields: List[dict]) -> dict:
        response = self.api_request(
            method='POST',
            endpoint=f'{self.base_endpoint}/setBotFields',
            params={
                'fields': fields,
            },
        )
        return response
