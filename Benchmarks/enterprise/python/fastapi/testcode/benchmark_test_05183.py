# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest05183(request: Request):
    path_value = request.path_params.get('id', '')
    request.session['data'] = str(path_value)
    return {"updated": True}
