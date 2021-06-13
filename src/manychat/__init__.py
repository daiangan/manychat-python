from dataclasses import dataclass, field

from .fb import Fb


@dataclass
class ManyChat:
    api_key: str
    fb: Fb = field(init=False)

    def __post_init__(self):
        self.fb = Fb(api_key=self.api_key)
