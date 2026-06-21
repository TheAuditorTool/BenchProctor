# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest22983(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    size = min(int(header_value) if str(header_value).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
