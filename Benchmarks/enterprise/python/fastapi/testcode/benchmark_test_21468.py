# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


async def BenchmarkTest21468(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = '{}'.format(ua_value)
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
