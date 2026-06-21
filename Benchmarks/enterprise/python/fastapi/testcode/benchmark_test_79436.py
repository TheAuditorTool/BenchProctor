# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


async def BenchmarkTest79436(request: Request):
    user_id = request.query_params.get('id', '')
    data = (lambda v: v.strip())(user_id)
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
