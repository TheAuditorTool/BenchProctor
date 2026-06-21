# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest32745(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = bytes.fromhex(auth_header).decode('utf-8', 'ignore')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
