# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest36037(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    def normalize(value):
        return value.strip()
    data = normalize(forwarded_ip)
    int(str(data))
    return {"updated": True}
