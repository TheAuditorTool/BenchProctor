# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest67040(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    if raw_body:
        data = raw_body
    else:
        data = ''
    int(str(data))
    return {"updated": True}
