# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest60994(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    if header_value:
        data = header_value
    else:
        data = ''
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
