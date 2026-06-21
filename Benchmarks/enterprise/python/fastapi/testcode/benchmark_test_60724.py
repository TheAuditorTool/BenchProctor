# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest60724(request: Request):
    path_value = request.path_params.get('id', '')
    data = '%s' % (path_value,)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
