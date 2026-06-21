# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import time


async def BenchmarkTest73765(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
