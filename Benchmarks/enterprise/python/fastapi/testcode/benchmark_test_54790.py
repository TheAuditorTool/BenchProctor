# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


async def BenchmarkTest54790(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = f'{raw_body:.200s}'
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
