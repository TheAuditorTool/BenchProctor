# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest48460(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '{}'.format(referer_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
