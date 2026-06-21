# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest45968(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value:.200s}'
    eval(str(data))
    return {"updated": True}
