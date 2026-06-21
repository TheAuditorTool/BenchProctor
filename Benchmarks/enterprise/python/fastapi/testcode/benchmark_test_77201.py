# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import unquote


async def BenchmarkTest77201(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
