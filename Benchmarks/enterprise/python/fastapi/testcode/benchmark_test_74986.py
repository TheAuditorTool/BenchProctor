# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest74986(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
