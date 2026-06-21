# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest63877(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value}'
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
