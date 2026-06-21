# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest39133(request: Request):
    origin_value = request.headers.get('origin', '')
    if origin_value:
        data = origin_value
    else:
        data = ''
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        pass
    return {"updated": True}
