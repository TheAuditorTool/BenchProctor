# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree
import json


async def BenchmarkTest44713(request: Request):
    ua_value = request.headers.get('user-agent', '')
    try:
        data = json.loads(ua_value).get('value', ua_value)
    except (json.JSONDecodeError, AttributeError):
        data = ua_value
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return {"updated": True}
