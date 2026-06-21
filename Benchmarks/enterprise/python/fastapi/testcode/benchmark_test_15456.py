# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import unquote


async def BenchmarkTest15456(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
