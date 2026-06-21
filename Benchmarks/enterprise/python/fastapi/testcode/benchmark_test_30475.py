# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest30475(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    eval(str(raw_body))
    return {"updated": True}
