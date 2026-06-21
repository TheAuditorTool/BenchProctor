# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest21823(request: Request):
    path_value = request.path_params.get('id', '')
    prefix = ''
    data = prefix + str(path_value)
    request.session['data'] = str(data)
    return {"updated": True}
