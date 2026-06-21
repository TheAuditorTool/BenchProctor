# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest05386(request: Request):
    path_value = request.path_params.get('id', '')
    parts = str(path_value).split(',')
    data = ','.join(parts)
    request.session['user'] = str(data)
    return {"updated": True}
