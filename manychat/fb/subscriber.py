from dataclasses import dataclass
from typing import List

from ..api import ManyChatAPI


@dataclass
class Subscriber(ManyChatAPI):
    api_key: str
    base_endpoint = "subscriber"

    def get_info(self, subscriber_id: str) -> dict:
        response = self.api_request(
            method="GET",
            endpoint=f"{self.base_endpoint}/getInfo",
            params={
                "subscriber_id": subscriber_id,
            },
        )
        return response

    def find_by_name(self, name: str) -> dict:
        response = self.api_request(
            method="GET",
            endpoint=f"{self.base_endpoint}/findByName",
            params={
                "name": name,
            },
        )
        return response

    def get_info_by_user_ref(self, user_ref: int) -> dict:
        response = self.api_request(
            method="GET",
            endpoint=f"{self.base_endpoint}/getInfoByUserRef",
            params={
                "user_ref": user_ref,
            },
        )
        return response

    def find_by_custom_field(self, field_id: int, field_value: str) -> dict:
        response = self.api_request(
            method="GET",
            endpoint=f"{self.base_endpoint}/findByCustomField",
            params={
                "field_id": field_id,
                "field_value": field_value,
            },
        )
        return response

    def find_by_system_field(self, email: str = None, phone: str = None) -> dict:
        if email is None and phone is None:
            return {"error": True, "message": "At least an email or a phone number must be provided."}

        params = {}
        if email is not None:
            params["email"] = email
        if phone is not None:
            params["phone"] = phone

        response = self.api_request(
            method="GET",
            endpoint=f"{self.base_endpoint}/findBySystemField",
            params=params,
        )
        return response

    def add_tag(self, subscriber_id: int, tag_id: int) -> dict:
        response = self.api_request(
            method="POST",
            endpoint=f"{self.base_endpoint}/addTag",
            params={
                "subscriber_id": subscriber_id,
                "tag_id": tag_id,
            },
        )
        return response

    def add_tag_by_name(self, subscriber_id: int, tag_name: str) -> dict:
        response = self.api_request(
            method="POST",
            endpoint=f"{self.base_endpoint}/addTagByName",
            params={
                "subscriber_id": subscriber_id,
                "tag_name": tag_name,
            },
        )
        return response

    def remove_tag(self, subscriber_id: int, tag_id: int) -> dict:
        response = self.api_request(
            method="POST",
            endpoint=f"{self.base_endpoint}/removeTag",
            params={
                "subscriber_id": subscriber_id,
                "tag_id": tag_id,
            },
        )
        return response

    def remove_tag_by_name(self, subscriber_id: int, tag_name: str) -> dict:
        response = self.api_request(
            method="POST",
            endpoint=f"{self.base_endpoint}/removeTagByName",
            params={
                "subscriber_id": subscriber_id,
                "tag_name": tag_name,
            },
        )
        return response

    def set_custom_field(self, subscriber_id: int, field_id: int, field_value: str) -> dict:
        response = self.api_request(
            method="POST",
            endpoint=f"{self.base_endpoint}/setCustomField",
            params={
                "subscriber_id": subscriber_id,
                "field_id": field_id,
                "field_value": field_value,
            },
        )
        return response

    def set_custom_fields(self, subscriber_id: int, fields: List[dict]) -> dict:
        response = self.api_request(
            method="POST",
            endpoint=f"{self.base_endpoint}/setCustomFields",
            params={
                "subscriber_id": subscriber_id,
                "fields": fields,
            },
        )
        return response

    def set_custom_field_by_name(self, subscriber_id: int, field_name: str, field_value: str) -> dict:
        response = self.api_request(
            method="POST",
            endpoint=f"{self.base_endpoint}/setCustomFieldByName",
            params={
                "subscriber_id": subscriber_id,
                "field_name": field_name,
                "field_value": field_value,
            },
        )
        return response

    def verify_by_signed_request(self, subscriber_id: int, signed_request: str) -> dict:
        response = self.api_request(
            method="POST",
            endpoint=f"{self.base_endpoint}/verifyBySignedRequest",
            params={
                "subscriber_id": subscriber_id,
                "signed_request": signed_request,
            },
        )
        return response

    def create_subscriber(
        self,
        first_name: str = None,
        last_name: str = None,
        phone: str = None,
        whatsapp_phone: str = None,
        email: str = None,
        gender: str = None,
        consent_phrase: str = None,
        has_opt_in_sms: bool = False,
        has_opt_in_email: bool = False,
    ) -> dict:
        params = {key: value for key, value in locals().items() if value and key != "self"}

        response = self.api_request(
            method="POST",
            endpoint=f"{self.base_endpoint}/createSubscriber",
            params=params,
        )
        return response

    def update_subscriber(
        self,
        subscriber_id: int,
        first_name: str = None,
        last_name: str = None,
        phone: str = None,
        email: str = None,
        gender: str = None,
        consent_phrase: str = None,
        has_opt_in_sms: bool = False,
        has_opt_in_email: bool = False,
    ) -> dict:
        params = {
            key: value
            for key, value in locals().items()
            if value and key not in ["self", "has_opt_in_sms", "has_opt_in_email"]
        }

        response = self.api_request(
            method="POST",
            endpoint=f"{self.base_endpoint}/updateSubscriber",
            params=params,
        )
        return response
