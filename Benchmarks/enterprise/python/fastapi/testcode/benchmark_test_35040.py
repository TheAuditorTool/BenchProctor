# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest35040(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
