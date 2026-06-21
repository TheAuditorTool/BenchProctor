# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest21153(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = ' '.join(str(header_value).split())
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
