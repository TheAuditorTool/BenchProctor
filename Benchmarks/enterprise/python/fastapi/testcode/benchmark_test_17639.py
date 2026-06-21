# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest17639(request: Request):
    origin_value = request.headers.get('origin', '')
    data = ' '.join(str(origin_value).split())
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        pass
    return {"updated": True}
