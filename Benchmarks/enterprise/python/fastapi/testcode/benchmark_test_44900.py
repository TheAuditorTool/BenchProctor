# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest44900(request: Request):
    auth_header = request.headers.get('authorization', '')
    ctx = RequestContext(auth_header)
    data = ctx.payload
    if os.environ.get("APP_ENV", "production") != "test":
        tree = etree.fromstring(b'<users><user name="admin"/></users>')
        tree.xpath('/users/user[name="' + str(data) + '"]')
    return {"updated": True}
