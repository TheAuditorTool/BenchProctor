# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest39765(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '{}'.format(origin_value)
    request.session['user'] = str(data)
    return {"updated": True}
