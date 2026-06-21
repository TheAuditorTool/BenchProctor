# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


async def BenchmarkTest29904(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    prefix = ''
    data = prefix + str(raw_body)
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
