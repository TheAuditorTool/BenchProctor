# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import time


@dataclass
class FormData:
    payload: str

async def BenchmarkTest56410(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = FormData(payload=auth_header).payload
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
