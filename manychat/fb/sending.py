from dataclasses import dataclass

from ..api import ManyChatAPI


@dataclass
class Sending(ManyChatAPI):
    api_key: str
    base_endpoint = 'sending'

    def send_content(self,
                     subscriber_id: int,
                     data: dict,
                     message_tag: str,
                     otn_topic_name: str) -> dict:
        response = self.api_request(
            method='POST',
            endpoint=f'{self.base_endpoint}/sendContent',
            params={
                'subscriber_id': subscriber_id,
                'data': data,
                'message_tag': message_tag,
                'otn_topic_name': otn_topic_name,
            },
        )
        return response

    def send_content_by_user_ref(self,
                                 user_ref: int,
                                 data: dict) -> dict:
        response = self.api_request(
            method='POST',
            endpoint=f'{self.base_endpoint}/sendContentByUserRef',
            params={
                'user_ref': user_ref,
                'data': data,
            },
        )
        return response

    def send_flow(self,
                  subscriber_id: int,
                  flow_ns: str):
        response = self.api_request(
            method='POST',
            endpoint=f'{self.base_endpoint}/sendFlow',
            params={
                'subscriber_id': subscriber_id,
                'flow_ns': flow_ns,
            },
        )
        return response
