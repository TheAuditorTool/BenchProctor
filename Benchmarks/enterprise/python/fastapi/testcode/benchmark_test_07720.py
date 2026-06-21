# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def relay_value(value):
    return value

async def BenchmarkTest07720(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = relay_value(forwarded_ip)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
