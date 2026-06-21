# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest12587(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '{}'.format(referer_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
