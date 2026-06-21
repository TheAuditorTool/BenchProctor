# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


async def BenchmarkTest00429(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '%s' % (referer_value,)
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
