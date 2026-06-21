# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


async def BenchmarkTest79978(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value:.200s}'
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
