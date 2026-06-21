# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


async def BenchmarkTest44124(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '%s' % (origin_value,)
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
