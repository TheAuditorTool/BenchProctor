# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest14899(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = f'{forwarded_ip}'
    os.remove(str(data))
    return {"updated": True}
