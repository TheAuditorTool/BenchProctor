# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def relay_value(value):
    return value

async def BenchmarkTest44980(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = relay_value(raw_body)
    request.session['data'] = str(data)
    return {"updated": True}
