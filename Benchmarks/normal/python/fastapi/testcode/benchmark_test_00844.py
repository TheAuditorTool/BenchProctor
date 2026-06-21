# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest00844(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = '%s' % str(header_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
