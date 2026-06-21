# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest67825(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = str(raw_body).replace('\x00', '')
    request.session['data'] = str(data)
    return {"updated": True}
