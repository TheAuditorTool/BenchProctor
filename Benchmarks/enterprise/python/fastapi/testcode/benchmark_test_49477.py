# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest49477(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = f'{auth_header}'
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
