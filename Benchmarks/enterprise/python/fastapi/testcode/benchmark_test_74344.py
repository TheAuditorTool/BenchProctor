# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest74344(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value}'
    requests.get(str(data))
    return {"updated": True}
