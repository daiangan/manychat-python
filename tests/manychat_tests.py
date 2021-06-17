import os

from src.manychat import ManyChat


mc = ManyChat(
    api_key=os.getenv('MANYCHAT_API_KEY')
)

# Page
# page = mc.fb.page
# page_info = mc.fb.page.get_info()
# page_info = page.get_info()
# tag = mc.fb.page.create_tag(tag_name='my_test_tag2')
# tags = mc.fb.page.get_tags()
# tag_to_remove = mc.fb.page.remove_tag(tag_id=28356445)
# custom_field = mc.fb.page.create_custom_field(
#     caption='api_test_created',
#     type='text',
#     description='This is just a test.'
# )
# growth_tools = mc.fb.page.get_growth_tools()
# flows = mc.fb.page.get_flows()
# cuf = mc.fb.page.get_custom_fields()
# otns = mc.fb.page.get_otn_topics()
# bot_fields = mc.fb.page.get_bot_fields()
# bot_field = mc.fb.page.create_bot_field(
#     name='test_bot_field',
#     type='text',
#     description='A test bot field.',
#     value='This is a test value',
# )
# bot_field = mc.fb.page.set_bot_field(
#     field_id=2464420,
#     field_value='New value',
# )
# bot_field = mc.fb.page.set_bot_field_by_name(
#     field_name='test_bot_field',
#     field_value='Other new value',
# )


# Sending
# send_flow = mc.fb.sending.send_flow(
#     subscriber_id=os.getenv('SUBSCRIBER_ID'),
#     flow_ns='content20210615114753_45563'
# )


# Subscriber
# subscriber_info = mc.fb.subscriber.get_info(
#     subscriber_id=os.getenv('SUBSCRIBER_ID'),
# )
# subscriber = mc.fb.subscriber.find_by_name(
#     name='Your Name'
# )
# subscriber = mc.fb.subscriber.get_info_by_user_ref(
#     user_ref=os.getenv('SUBSCRIBER_ID'),
# )




