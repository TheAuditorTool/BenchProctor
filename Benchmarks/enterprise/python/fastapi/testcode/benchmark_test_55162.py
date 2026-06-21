# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest55162(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = f'{forwarded_ip:.200s}'
    os.remove(str(data))
    return {"updated": True}
