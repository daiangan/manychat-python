from dataclasses import dataclass

@dataclass
class Sending:
    api_key: str

    def send_flow(self):
        print('send flow')

