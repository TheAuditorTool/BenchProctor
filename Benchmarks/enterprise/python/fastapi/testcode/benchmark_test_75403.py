# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


async def BenchmarkTest75403(request: Request):
    user_id = request.query_params.get('id', '')
    data = ' '.join(str(user_id).split())
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
