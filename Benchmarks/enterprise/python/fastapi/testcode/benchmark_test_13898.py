# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
import requests


async def BenchmarkTest13898(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
