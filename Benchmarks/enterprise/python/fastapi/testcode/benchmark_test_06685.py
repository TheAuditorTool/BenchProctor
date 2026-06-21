# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest06685(request: Request):
    host_value = request.headers.get('host', '')
    data = f'{host_value:.200s}'
    requests.get(str(data))
    return {"updated": True}
