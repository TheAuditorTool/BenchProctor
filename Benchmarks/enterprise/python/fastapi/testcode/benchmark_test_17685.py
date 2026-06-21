# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest17685(request: Request):
    path_value = request.path_params.get('id', '')
    data = '%s' % str(path_value)
    int(str(data))
    return {"updated": True}
