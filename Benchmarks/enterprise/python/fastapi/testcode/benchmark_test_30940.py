# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest30940(request: Request):
    path_value = request.path_params.get('id', '')
    parts = str(path_value).split(',')
    data = ','.join(parts)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
