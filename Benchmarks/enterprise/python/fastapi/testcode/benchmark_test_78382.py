# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


def relay_value(value):
    return value

async def BenchmarkTest78382(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = relay_value(upload_name)
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
