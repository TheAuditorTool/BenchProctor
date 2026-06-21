# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest55603(request: Request):
    origin_value = request.headers.get('origin', '')
    requests.post('http://api.prod.internal/data', data=str(origin_value))
    return {"updated": True}
