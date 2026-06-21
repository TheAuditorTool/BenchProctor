# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def normalise_input(value):
    return value.strip()

async def BenchmarkTest14184(request: Request):
    referer_value = request.headers.get('referer', '')
    data = normalise_input(referer_value)
    request.session['data'] = str(data)
    return {"updated": True}
