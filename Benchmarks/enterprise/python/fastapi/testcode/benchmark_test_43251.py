# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest43251(request: Request):
    path_value = request.path_params.get('id', '')
    data = str(path_value).replace('\x00', '')
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
