# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest40908(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = f'{raw_body}'
    request.session['data'] = str(data)
    return {"updated": True}
