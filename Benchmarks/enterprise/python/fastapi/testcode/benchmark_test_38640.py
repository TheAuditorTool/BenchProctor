# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest38640(request: Request):
    path_value = request.path_params.get('id', '')
    parts = str(path_value).split(',')
    data = ','.join(parts)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
