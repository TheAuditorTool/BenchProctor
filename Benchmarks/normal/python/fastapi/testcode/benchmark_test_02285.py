# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest02285(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = ' '.join(str(header_value).split())
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
