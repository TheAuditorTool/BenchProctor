# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest01722(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = '{}'.format(ua_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
