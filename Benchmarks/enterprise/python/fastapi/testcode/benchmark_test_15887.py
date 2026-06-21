# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request


request_state: dict[str, str] = {}

async def BenchmarkTest15887(request: Request):
    path_value = request.path_params.get('id', '')
    request_state['last_input'] = path_value
    data = request_state['last_input']
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
