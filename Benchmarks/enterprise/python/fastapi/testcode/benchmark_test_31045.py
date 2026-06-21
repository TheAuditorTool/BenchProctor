# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest31045(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = '%s' % (forwarded_ip,)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return {"updated": True}
