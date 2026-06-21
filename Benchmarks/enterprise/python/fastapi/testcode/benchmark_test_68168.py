# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


async def BenchmarkTest68168(request: Request):
    auth_header = request.headers.get('authorization', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
