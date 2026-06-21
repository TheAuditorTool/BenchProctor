# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


def relay_value(value):
    return value

async def BenchmarkTest29164(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = relay_value(cookie_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
