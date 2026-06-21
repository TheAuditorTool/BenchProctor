# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest37471(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = ' '.join(str(forwarded_ip).split())
    int(str(data))
    return {"updated": True}
