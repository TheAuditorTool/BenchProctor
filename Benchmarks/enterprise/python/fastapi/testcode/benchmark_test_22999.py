# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest22999(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value}'
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
