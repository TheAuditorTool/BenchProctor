# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest55746(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value}'
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
