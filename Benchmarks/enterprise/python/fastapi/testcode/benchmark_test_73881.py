# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest73881(request: Request):
    path_value = request.path_params.get('id', '')
    data = path_value if path_value else 'default'
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
