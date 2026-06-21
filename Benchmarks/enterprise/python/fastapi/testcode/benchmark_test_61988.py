# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def to_text(value):
    return str(value).strip()

async def BenchmarkTest61988(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = to_text(auth_header)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
