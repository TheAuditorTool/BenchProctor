# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


async def BenchmarkTest65157(request: Request):
    path_value = request.path_params.get('id', '')
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(path_value)
    return {"updated": True}
