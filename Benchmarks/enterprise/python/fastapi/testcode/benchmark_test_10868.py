# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest10868(request: Request):
    auth_header = request.headers.get('authorization', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    os.remove(str(data))
    return {"updated": True}
