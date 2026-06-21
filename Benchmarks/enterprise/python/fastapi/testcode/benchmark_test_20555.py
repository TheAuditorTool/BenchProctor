# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


async def BenchmarkTest20555(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(cookie_value) + '"]')
    return {"updated": True}
