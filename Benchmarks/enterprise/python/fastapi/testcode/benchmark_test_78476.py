# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest78476(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    ctx = RequestContext(cookie_value)
    data = ctx.payload
    if os.environ.get("APP_ENV", "production") != "test":
        yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
