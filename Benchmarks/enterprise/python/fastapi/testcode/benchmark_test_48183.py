# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest48183(request: Request):
    referer_value = request.headers.get('referer', '')
    data = str(referer_value).replace('\x00', '')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
