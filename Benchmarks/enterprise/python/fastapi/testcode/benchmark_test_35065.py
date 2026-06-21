# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest35065(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    os.remove(str(raw_body))
    return {"updated": True}
