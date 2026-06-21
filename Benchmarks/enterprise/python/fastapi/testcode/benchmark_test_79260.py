# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


async def BenchmarkTest79260(request: Request):
    path_value = request.path_params.get('id', '')
    data, _sep, _rest = str(path_value).partition('\x00')
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
