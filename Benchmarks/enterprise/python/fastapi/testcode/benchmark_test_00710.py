# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest00710(request: Request):
    origin_value = request.headers.get('origin', '')
    requests.post('https://api.prod.internal/data', data=str(origin_value), verify=True)
    return {"updated": True}
