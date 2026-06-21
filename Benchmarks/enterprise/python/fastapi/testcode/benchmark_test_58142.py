# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest58142(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = '{}'.format(raw_body)
    eval(str(data))
    return {"updated": True}
