# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest68976(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = bytes.fromhex(auth_header).decode('utf-8', 'ignore')
    os.remove(str(data))
    return {"updated": True}
