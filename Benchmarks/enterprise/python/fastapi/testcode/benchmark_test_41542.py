# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest41542(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '{}'.format(origin_value)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
