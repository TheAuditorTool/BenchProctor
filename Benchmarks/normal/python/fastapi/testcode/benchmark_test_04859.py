# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest04859(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = str(forwarded_ip).replace('\x00', '')
    json.loads(data)
    return {"updated": True}
