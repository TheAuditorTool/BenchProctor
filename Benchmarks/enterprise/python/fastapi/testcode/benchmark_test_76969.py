# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest76969(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    if forwarded_ip:
        data = forwarded_ip
    else:
        data = ''
    os.remove(str(data))
    return {"updated": True}
