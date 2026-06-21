# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest61540(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '%s' % (origin_value,)
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
