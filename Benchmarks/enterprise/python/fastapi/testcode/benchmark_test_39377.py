# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest39377(request: Request):
    host_value = request.headers.get('host', '')
    data = f'{host_value}'
    requests.get(str(data))
    return {"updated": True}
