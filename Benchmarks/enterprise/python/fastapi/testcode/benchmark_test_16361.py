# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest16361(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = ' '.join(str(cookie_value).split())
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
