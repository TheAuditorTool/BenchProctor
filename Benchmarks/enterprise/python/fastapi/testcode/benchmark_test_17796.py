# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest17796(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    try:
        os.setuid(int(str(raw_body)) if str(raw_body).isdigit() else 65534)
    except OSError:
        pass
    return {"updated": True}
