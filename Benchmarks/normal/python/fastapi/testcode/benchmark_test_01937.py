# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest01937(request: Request):
    origin_value = request.headers.get('origin', '')
    data = origin_value if origin_value else 'default'
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return {"updated": True}
