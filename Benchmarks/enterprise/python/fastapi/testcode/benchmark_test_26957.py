# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
import time


async def BenchmarkTest26957(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
