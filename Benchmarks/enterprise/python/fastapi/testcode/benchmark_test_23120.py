# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest23120(request: Request):
    path_value = request.path_params.get('id', '')
    data = ' '.join(str(path_value).split())
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
