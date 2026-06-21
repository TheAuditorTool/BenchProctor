# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest43897(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = raw_body.decode('utf-8', 'ignore') if isinstance(raw_body, bytes) else raw_body
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
