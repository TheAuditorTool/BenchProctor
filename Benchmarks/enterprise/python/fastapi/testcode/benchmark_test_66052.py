# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest66052(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = bytearray(int(ua_value) if str(ua_value).isdigit() else 0)
    return {"updated": True}
