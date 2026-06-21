# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def ensure_str(value):
    return str(value)

async def BenchmarkTest50865(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = ensure_str(auth_header)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
