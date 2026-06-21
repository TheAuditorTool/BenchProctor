# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


async def BenchmarkTest73293(request: Request):
    path_value = request.path_params.get('id', '')
    if path_value:
        data = path_value
    else:
        data = ''
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
