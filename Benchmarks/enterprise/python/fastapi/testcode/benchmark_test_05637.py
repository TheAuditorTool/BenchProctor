# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest05637(request: Request):
    host_value = request.headers.get('host', '')
    data = host_value if host_value else 'default'
    requests.get(str(data))
    return {"updated": True}
