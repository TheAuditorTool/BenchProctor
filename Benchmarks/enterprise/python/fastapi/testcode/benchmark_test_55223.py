# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest55223(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value:.200s}'
    request.session['data'] = str(data)
    return {"updated": True}
