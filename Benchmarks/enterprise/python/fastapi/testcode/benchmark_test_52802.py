# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest52802(request: Request):
    origin_value = request.headers.get('origin', '')
    data = ' '.join(str(origin_value).split())
    request.session['data'] = str(data)
    return {"updated": True}
