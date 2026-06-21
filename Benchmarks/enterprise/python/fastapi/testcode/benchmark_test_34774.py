# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest34774(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '%s' % str(auth_header)
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
