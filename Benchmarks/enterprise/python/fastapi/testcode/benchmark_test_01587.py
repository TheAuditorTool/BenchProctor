# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest01587(request: Request):
    origin_value = request.headers.get('origin', '')
    data = origin_value if origin_value else 'default'
    request.session['data'] = str(data)
    return {"updated": True}
