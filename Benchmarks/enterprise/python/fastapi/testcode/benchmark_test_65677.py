# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


async def BenchmarkTest65677(request: Request):
    origin_value = request.headers.get('origin', '')
    data, _sep, _rest = str(origin_value).partition('\x00')
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
