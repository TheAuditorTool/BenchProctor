# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


async def BenchmarkTest41018(request: Request):
    path_value = request.path_params.get('id', '')
    data = ' '.join(str(path_value).split())
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
