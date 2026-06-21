# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest40844(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    parts = str(raw_body).split(',')
    data = ','.join(parts)
    request.session['user'] = str(data)
    return {"updated": True}
