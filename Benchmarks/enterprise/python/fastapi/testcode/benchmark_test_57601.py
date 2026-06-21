# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest57601(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = coalesce_blank(cookie_value)
    json.loads(data)
    return {"updated": True}
