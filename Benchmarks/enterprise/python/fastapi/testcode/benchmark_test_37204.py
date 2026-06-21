# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest37204(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = raw_body if raw_body else 'default'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
