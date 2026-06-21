# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


async def BenchmarkTest20163(request: Request):
    host_value = request.headers.get('host', '')
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(host_value)
    return {"updated": True}
