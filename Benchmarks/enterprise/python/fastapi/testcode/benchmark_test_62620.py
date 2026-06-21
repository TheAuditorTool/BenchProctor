# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest62620(request: Request):
    origin_value = request.headers.get('origin', '')
    parts = str(origin_value).split(',')
    data = ','.join(parts)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
