# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest19791(request: Request):
    path_value = request.path_params.get('id', '')
    data = path_value if path_value else 'default'
    request.session['data'] = str(data)
    return {"updated": True}
