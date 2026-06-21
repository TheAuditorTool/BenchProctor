# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


async def BenchmarkTest02823(request: Request):
    host_value = request.headers.get('host', '')
    data = '%s' % (host_value,)
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
