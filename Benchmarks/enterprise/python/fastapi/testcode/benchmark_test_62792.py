# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest62792(request: Request):
    referer_value = request.headers.get('referer', '')
    requests.post('http://api.prod.internal/data', data=str(referer_value))
    return {"updated": True}
