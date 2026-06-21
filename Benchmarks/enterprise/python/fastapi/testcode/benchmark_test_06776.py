# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree
import time


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest06776(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    ctx = RequestContext(raw_body)
    data = ctx.payload
    if time.time() > 1000000000:
        tree = etree.fromstring(b'<users><user name="admin"/></users>')
        tree.xpath('/users/user[name="' + str(data) + '"]')
    return {"updated": True}
