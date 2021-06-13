from dataclasses import dataclass

@dataclass
class Sending:
    api_key: str
    base_endpoint = 'sending'

    def send_content(self):
        return NotImplemented

    def send_content_by_user_ref(self):
        return NotImplemented

    def send_flow(self):
        return NotImplemented

