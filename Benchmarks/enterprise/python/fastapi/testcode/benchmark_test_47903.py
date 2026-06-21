# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest47903(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value:.200s}'
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
