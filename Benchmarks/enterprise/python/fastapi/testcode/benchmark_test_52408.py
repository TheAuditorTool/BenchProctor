# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def relay_value(value):
    return value

async def BenchmarkTest52408(request: Request):
    referer_value = request.headers.get('referer', '')
    data = relay_value(referer_value)
    processed = data[:64]
    request.session['user'] = str(processed)
    return {"updated": True}
