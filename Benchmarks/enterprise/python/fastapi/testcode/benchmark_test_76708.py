# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def relay_value(value):
    return value

async def BenchmarkTest76708(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = relay_value(raw_body)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
