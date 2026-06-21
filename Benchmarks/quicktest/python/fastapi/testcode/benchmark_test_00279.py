# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest00279(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    if forwarded_ip:
        data = forwarded_ip
    else:
        data = ''
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
