# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest73896(request: Request):
    path_value = request.path_params.get('id', '')
    if path_value:
        data = path_value
    else:
        data = ''
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
