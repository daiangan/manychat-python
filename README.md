# manychat-python
![](https://img.shields.io/badge/version-0.1.4-success) ![](https://img.shields.io/badge/Python-3.8%20|%203.9%20|%203.10%20|%203.11-4B8BBE?logo=python&logoColor=white)

This is an unofficial Python package for an easy use of the [ManyChat API.](https://api.manychat.com/)

#### Installation
```text
pip install manychat-python
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
    flow_ns='content20210489114753_47763' # this is just an example
)
# Subscriber
subscriber_info = mc.fb.subscriber.get_info(
    subscriber_id='SUBSCRIBER_ID'
)
```
To see more examples, please go to: [tests/manychat_tests.py](https://github.com/daiangan/manychat-python/blob/main/tests/manychat_tests.py)

GitHub Repo: [https://github.com/daiangan/manychat-python](https://github.com/daiangan/manychat-python)

#### Some Notes:
All methods are named using the Python function naming rules: lowercase with words separated by underscores as necessary to improve readability.
<br>
So, for example, the ManyChat endpoint __/fb/sending/sendFlow__ is translated to: __fb.sending.send_flow()__
<br>
More info about [Style Guide for Python Code.](https://www.python.org/dev/peps/pep-0008/#function-and-variable-names)
<br>

Please read the official ManyChat API Documentation for more details:
[https://api.manychat.com/](https://api.manychat.com/)
<br>

#### About this project

This project is a **clone** of the project created and maintained by:
__Daian Gan__  
Github: [daiangan](https://github.com/daiangan)  
E-mail: daian@ganmedia.com  
Website: https://daiangan.com  