# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest29860(request: Request):
    origin_value = request.headers.get('origin', '')
    kind = 'json' if str(origin_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = origin_value
            data = parsed
        case _:
            data = origin_value
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
