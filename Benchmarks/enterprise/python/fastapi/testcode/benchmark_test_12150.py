# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest12150(request: Request):
    origin_value = request.headers.get('origin', '')
    data = str(origin_value).replace('\x00', '')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
