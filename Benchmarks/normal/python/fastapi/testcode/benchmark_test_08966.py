# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest08966(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    json.loads(forwarded_ip)
    return {"updated": True}
