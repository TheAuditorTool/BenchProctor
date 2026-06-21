# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import unquote


async def BenchmarkTest43493(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
