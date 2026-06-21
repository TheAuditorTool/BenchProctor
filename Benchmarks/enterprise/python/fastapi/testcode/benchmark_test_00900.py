# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest00900(request: Request):
    path_value = request.path_params.get('id', '')
    data = path_value if path_value else 'default'
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
