# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest34125(request: Request):
    path_value = request.path_params.get('id', '')
    data = '%s' % (path_value,)
    request.session['data'] = str(data)
    return {"updated": True}
