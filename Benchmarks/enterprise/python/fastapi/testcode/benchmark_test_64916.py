# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest64916(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    if raw_body:
        data = raw_body
    else:
        data = ''
    request.session['data'] = str(data)
    return {"updated": True}
