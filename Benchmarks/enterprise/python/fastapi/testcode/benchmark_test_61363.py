# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest61363(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = ua_value if ua_value else 'default'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
