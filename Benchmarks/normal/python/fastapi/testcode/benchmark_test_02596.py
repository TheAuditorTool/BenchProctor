# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest02596(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    if raw_body:
        data = raw_body
    else:
        data = ''
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
