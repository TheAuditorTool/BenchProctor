# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest02389(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = str(raw_body).replace('\x00', '')
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        pass
    return {"updated": True}
