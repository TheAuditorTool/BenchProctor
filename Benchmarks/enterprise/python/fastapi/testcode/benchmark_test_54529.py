# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import base64


async def BenchmarkTest54529(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    requests.get(str(data))
    return {"updated": True}
