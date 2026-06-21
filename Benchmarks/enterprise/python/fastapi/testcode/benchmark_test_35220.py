# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


async def BenchmarkTest35220(request: Request):
    referer_value = request.headers.get('referer', '')
    parts = str(referer_value).split(',')
    data = ','.join(parts)
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
