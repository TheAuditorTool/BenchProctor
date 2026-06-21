# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


async def BenchmarkTest70843(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = '{}'.format(xml_value)
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
