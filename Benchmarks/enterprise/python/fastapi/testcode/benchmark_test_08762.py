# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest08762(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = bytearray(int(raw_body) if str(raw_body).isdigit() else 0)
    return {"updated": True}
