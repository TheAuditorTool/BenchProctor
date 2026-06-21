# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
import time


async def BenchmarkTest02305(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
