# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest45078(request: Request):
    auth_header = request.headers.get('authorization', '')
    requests.post('http://api.prod.internal/data', data=str(auth_header))
    return {"updated": True}
