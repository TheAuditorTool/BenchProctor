# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import time


@dataclass
class FormData:
    payload: str

async def BenchmarkTest46418(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = FormData(payload=raw_body).payload
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
