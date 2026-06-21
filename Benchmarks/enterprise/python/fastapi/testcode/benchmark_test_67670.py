# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest67670(request: Request):
    path_value = request.path_params.get('id', '')
    data = ' '.join(str(path_value).split())
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
