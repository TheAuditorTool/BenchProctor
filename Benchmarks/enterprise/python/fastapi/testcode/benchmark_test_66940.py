# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest66940(request: Request):
    auth_header = request.headers.get('authorization', '')
    requests.post('https://api.prod.internal/data', data=str(auth_header), verify=True)
    return {"updated": True}
