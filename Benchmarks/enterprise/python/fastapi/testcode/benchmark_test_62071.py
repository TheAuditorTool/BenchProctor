# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


async def BenchmarkTest62071(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
