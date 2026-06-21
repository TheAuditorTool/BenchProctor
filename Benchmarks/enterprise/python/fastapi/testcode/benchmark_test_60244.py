# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest60244(request: Request):
    auth_header = request.headers.get('authorization', '')
    try:
        os.setuid(int(str(auth_header)) if str(auth_header).isdigit() else 65534)
    except OSError:
        pass
    return {"updated": True}
