# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest71219(request: Request):
    referer_value = request.headers.get('referer', '')
    data = default_blank(referer_value)
    request.session['data'] = str(data)
    return {"updated": True}
