# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest58009(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = ' '.join(str(ua_value).split())
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
