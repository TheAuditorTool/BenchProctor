# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest57605(request: Request):
    auth_header = request.headers.get('authorization', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    os.system('echo ' + str(data))
    return {"updated": True}
