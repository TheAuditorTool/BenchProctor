# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest28441(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value}'
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
