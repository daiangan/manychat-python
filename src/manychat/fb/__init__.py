from dataclasses import dataclass, field

from .page import Page
from .sending import Sending
from .subscriber import Subscriber


@dataclass
class Fb:
    api_key: str
    page: Page = field(init=False)
    sending: Sending = field(init=False)
    subscriber: Subscriber = field(init=False)

    def __post_init__(self):
        self.page = Page(api_key=self.api_key)
        self.sending = Sending(api_key=self.api_key)
        self.subscriber = Subscriber(api_key=self.api_key)
