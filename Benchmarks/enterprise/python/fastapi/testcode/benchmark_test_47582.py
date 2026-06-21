# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest47582(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = bytearray(int(auth_header) if str(auth_header).isdigit() else 0)
    return {"updated": True}
