# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def to_text(value):
    return str(value).strip()

async def BenchmarkTest78764(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = to_text(forwarded_ip)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
