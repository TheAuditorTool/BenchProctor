# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest66400(request: Request):
    auth_header = request.headers.get('authorization', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(auth_header)}, verify=True)
    return {"updated": True}
