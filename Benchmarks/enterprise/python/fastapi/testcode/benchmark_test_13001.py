# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest13001(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    requests.post('https://api.prod.internal/data', data=str(cookie_value), verify=True)
    return {"updated": True}
