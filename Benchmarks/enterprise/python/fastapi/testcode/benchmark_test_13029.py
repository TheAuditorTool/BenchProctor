# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest13029(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = ' '.join(str(raw_body).split())
    eval(str(data))
    return {"updated": True}
