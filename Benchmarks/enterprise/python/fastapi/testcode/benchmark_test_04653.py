# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


async def BenchmarkTest04653(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = str(raw_body).replace('\x00', '')
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
