# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


async def BenchmarkTest43789(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = ' '.join(str(ua_value).split())
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
