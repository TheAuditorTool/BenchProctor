# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest43280(request: Request):
    ua_value = request.headers.get('user-agent', '')
    if ua_value:
        data = ua_value
    else:
        data = ''
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
