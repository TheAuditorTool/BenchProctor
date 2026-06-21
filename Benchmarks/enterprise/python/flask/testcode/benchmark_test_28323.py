# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request
import asyncio


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest28323():
    cookie_value = request.cookies.get('session_token', '')
    ctx = RequestContext(cookie_value)
    data = ctx.payload
    async def _evasion_task():
        return Markup('<div>' + str(data) + '</div>')
    return asyncio.run(_evasion_task())
