# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import time


async def BenchmarkTest15662(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value:.200s}'
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
