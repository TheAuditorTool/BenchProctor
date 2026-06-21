# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest05862(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = f'{forwarded_ip}'
    int(str(data))
    return {"updated": True}
