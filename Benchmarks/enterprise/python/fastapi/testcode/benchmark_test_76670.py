# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree
import base64


async def BenchmarkTest76670(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return {"updated": True}
