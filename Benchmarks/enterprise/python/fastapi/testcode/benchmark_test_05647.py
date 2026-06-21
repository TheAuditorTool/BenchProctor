# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest05647(request: Request):
    origin_value = request.headers.get('origin', '')
    parts = str(origin_value).split(',')
    data = ','.join(parts)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
