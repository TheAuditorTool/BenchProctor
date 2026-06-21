# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


async def BenchmarkTest52289(request: Request):
    referer_value = request.headers.get('referer', '')
    data = ' '.join(str(referer_value).split())
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
