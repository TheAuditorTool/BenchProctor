# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


async def BenchmarkTest74033(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = '%s' % (raw_body,)
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
