# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import unquote


async def BenchmarkTest10743(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
