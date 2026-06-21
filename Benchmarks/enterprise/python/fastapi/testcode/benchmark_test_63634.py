# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


def relay_value(value):
    return value

async def BenchmarkTest63634(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = relay_value(forwarded_ip)
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
