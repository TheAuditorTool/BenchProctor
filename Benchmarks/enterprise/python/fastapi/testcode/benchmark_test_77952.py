# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest77952(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = bytes.fromhex(header_value).decode('utf-8', 'ignore')
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
