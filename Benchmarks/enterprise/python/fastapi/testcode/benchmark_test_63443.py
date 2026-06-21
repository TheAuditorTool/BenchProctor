# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest63443(request: Request):
    origin_value = request.headers.get('origin', '')
    data = default_blank(origin_value)
    request.session['data'] = str(data)
    return {"updated": True}
