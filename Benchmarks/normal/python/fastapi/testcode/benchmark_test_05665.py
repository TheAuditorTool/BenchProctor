# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest05665(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    requests.post('http://api.prod.internal/data', data=str(cookie_value))
    return {"updated": True}
