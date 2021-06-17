# ManyChat Python Package

This is a Python package for an easy use of the ManyChat API.

#### Installation
```text
pip install manychat
```
#### Usage
```python
from manychat import ManyChat

mc = ManyChat('YOUR_MANYCHAT_API_KEY')

# Page
page_info = mc.fb.page.get_info()

# Sending
send_flow = mc.fb.sending.send_flow(
    subscriber_id='SUBSCRIBER_ID',
    flow_ns='content20210489114753_47763'
)

# Subscriber
subscriber_info = mc.fb.subscriber.get_info(
    subscriber_id='SUBSCRIBER_ID'
)

```
To see more examples, please go to: [tests/manychat_tests.py](tests/manychat_tests.py)

#### Some Notes
All methods are named using the Python function naming rules: lowercase with words separated by underscores as necessary to improve readability.
<br>
So, for example, the ManyChat endpoint __/fb/sending/sendFlow__ is translated to: __fb.sending.send_flow()__
<br>
More info about [Style Guide for Python Code.](https://www.python.org/dev/peps/pep-0008/#function-and-variable-names)
<br>
<br>
Please read the official ManyChat API Documentation:
<br>
[https://api.manychat.com/](https://api.manychat.com/)
