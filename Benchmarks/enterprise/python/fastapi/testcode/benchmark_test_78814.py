# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest78814(request: Request):
    path_value = request.path_params.get('id', '')
    data = path_value if path_value else 'default'
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
