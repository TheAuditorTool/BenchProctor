# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest03749(request: Request):
    path_value = request.path_params.get('id', '')
    data = '{}'.format(path_value)
    request.session['data'] = str(data)
    return {"updated": True}
