# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def to_text(value):
    return str(value).strip()

async def BenchmarkTest10844(request: Request):
    origin_value = request.headers.get('origin', '')
    data = to_text(origin_value)
    request.session['user'] = str(data)
    return {"updated": True}
