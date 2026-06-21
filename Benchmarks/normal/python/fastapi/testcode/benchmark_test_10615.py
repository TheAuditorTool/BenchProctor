# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest10615(request: Request):
    path_value = request.path_params.get('id', '')
    data = '{}'.format(path_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
