# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest72505(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = (lambda v: v.strip())(raw_body)
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        pass
    return {"updated": True}
