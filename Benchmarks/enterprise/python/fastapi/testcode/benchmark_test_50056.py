# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest50056(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = (lambda v: v.strip())(header_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
