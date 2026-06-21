# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request
import asyncio


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest42393():
    header_value = request.headers.get('X-Custom-Header', '')
    ctx = RequestContext(header_value)
    data = ctx.payload
    async def _evasion_task():
        return Markup('<div>' + str(data) + '</div>')
    return asyncio.run(_evasion_task())
