# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree
import base64


async def BenchmarkTest27096(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return {"updated": True}
