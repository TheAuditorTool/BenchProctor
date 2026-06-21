# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest71815(request: Request):
    host_value = request.headers.get('host', '')
    data = '%s' % str(host_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
