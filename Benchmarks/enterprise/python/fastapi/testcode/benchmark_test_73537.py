# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest73537(request: Request):
    host_value = request.headers.get('host', '')
    data = ' '.join(str(host_value).split())
    requests.get(str(data))
    return {"updated": True}
