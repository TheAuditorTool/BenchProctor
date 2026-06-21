# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest61295(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    result = 100 / int(str(raw_body))
    return {"updated": True}
