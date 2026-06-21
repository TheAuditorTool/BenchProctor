# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest64910(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = bytes.fromhex(auth_header).decode('utf-8', 'ignore')
    result = 100 / int(str(data))
    return {"updated": True}
