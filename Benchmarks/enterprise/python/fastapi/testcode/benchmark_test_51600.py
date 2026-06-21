# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time


async def BenchmarkTest51600(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = '%s' % str(xml_value)
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
