# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest74192(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = f'{raw_body:.200s}'
    os.remove(str(data))
    return {"updated": True}
