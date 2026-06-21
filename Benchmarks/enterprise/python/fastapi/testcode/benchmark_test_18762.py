# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest18762(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '%s' % (origin_value,)
    request.session['user'] = str(data)
    return {"updated": True}
