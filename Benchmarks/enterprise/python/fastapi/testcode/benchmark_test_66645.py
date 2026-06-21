# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


async def BenchmarkTest66645(request: Request):
    host_value = request.headers.get('host', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
