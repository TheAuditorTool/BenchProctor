# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest30129(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = str(raw_body).replace('\x00', '')
    os.remove(str(data))
    return {"updated": True}
