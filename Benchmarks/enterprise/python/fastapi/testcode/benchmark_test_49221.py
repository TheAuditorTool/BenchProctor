# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest49221(request: Request):
    path_value = request.path_params.get('id', '')
    prefix = ''
    data = prefix + str(path_value)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
