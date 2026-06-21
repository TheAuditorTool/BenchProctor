# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from lxml import etree


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest46592(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    eval(compile('_parser = etree.XMLParser(resolve_entities=True, no_network=False)\netree.fromstring(str(data).encode(), _parser)', '<sink>', 'exec'))
    return {"updated": True}
