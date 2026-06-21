# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest33852(request: Request):
    host_value = request.headers.get('host', '')
    data = ' '.join(str(host_value).split())
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return {"updated": True}
