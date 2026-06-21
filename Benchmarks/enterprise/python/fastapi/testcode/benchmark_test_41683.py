# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64


async def BenchmarkTest41683(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
