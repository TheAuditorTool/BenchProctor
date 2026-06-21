# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
import time


async def BenchmarkTest42511(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
