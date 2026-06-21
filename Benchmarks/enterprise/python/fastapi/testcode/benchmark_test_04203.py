# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


async def BenchmarkTest04203(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data, _sep, _rest = str(header_value).partition('\x00')
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
