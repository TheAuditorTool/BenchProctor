# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest06277(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data, _sep, _rest = str(raw_body).partition('\x00')
    exec(str(data))
    return {"updated": True}
