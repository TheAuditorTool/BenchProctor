# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest38520(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = bytes.fromhex(auth_header).decode('utf-8', 'ignore')
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return {"updated": True}
