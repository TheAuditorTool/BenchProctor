# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


def relay_value(value):
    return value

async def BenchmarkTest44416(request: Request):
    host_value = request.headers.get('host', '')
    data = relay_value(host_value)
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
