# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest39758(request: Request):
    path_value = request.path_params.get('id', '')
    if path_value:
        data = path_value
    else:
        data = ''
    request.session['data'] = str(data)
    return {"updated": True}
