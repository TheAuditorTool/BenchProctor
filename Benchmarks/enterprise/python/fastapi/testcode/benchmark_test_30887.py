# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest30887(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    def normalize(value):
        return value.strip()
    data = normalize(raw_body)
    os.remove(str(data))
    return {"updated": True}
