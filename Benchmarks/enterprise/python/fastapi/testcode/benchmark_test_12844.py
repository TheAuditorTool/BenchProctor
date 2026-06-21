# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest12844(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    requests.post('https://api.prod.internal/data', data=str(header_value), verify=True)
    return {"updated": True}
