# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading


async def BenchmarkTest33868(request: Request):
    host_value = request.headers.get('host', '')
    data = host_value if host_value else 'default'
    globals()['counter'] = int(data)
    return {"updated": True}
