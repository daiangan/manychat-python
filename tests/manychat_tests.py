import os

from src.manychat import ManyChat


mc = ManyChat(
    api_key=os.getenv('MANYCHAT_API_KEY')
)

# Page
# page_info = mc.fb.page.get_info()
new_tag = mc.fb.page.create_tag()


# Subscriber
# subscriber_info = mc.fb.subscriber.get_info(
#     subscriber_id=os.getenv('SUBSCRIBER_ID'),
# )


print(new_tag)
