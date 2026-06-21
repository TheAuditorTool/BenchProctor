# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest58773(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = f'{ua_value}'
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return {"updated": True}
