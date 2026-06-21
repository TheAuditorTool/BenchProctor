# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest74098(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data, _sep, _rest = str(raw_body).partition('\x00')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
