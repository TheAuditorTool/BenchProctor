# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest72025(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value:.200s}'
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
