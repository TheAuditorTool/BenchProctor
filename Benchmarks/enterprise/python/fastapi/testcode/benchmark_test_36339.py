# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


async def BenchmarkTest36339(request: Request):
    host_value = request.headers.get('host', '')
    data = host_value if host_value else 'default'
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
