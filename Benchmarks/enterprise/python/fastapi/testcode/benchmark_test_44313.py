# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest44313(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = (lambda v: v.strip())(forwarded_ip)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
