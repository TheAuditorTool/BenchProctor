# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest50784(request: Request):
    host_value = request.headers.get('host', '')
    data = f'{host_value}'
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
