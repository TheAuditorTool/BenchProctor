# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest39307(request: Request):
    host_value = request.headers.get('host', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
