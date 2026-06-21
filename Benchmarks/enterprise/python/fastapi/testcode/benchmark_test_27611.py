# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import time


@dataclass
class FormData:
    payload: str

async def BenchmarkTest27611(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = FormData(payload=header_value).payload
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
