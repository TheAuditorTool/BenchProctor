# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest61711(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = (lambda v: v.strip())(ua_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
