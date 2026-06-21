# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


async def BenchmarkTest32478(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = f'{upload_name:.200s}'
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
