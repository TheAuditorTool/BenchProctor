# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


async def BenchmarkTest55613(request: Request):
    auth_header = request.headers.get('authorization', '')
    prefix = ''
    data = prefix + str(auth_header)
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
