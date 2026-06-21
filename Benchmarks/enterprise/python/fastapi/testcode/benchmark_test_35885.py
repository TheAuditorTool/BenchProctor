# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest35885(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '%s' % (auth_header,)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
