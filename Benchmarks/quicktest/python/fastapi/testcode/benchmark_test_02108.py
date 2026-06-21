# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest02108(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = bytes.fromhex(header_value).decode('utf-8', 'ignore')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
