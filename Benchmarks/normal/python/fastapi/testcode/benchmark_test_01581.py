# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest01581(request: Request):
    path_value = request.path_params.get('id', '')
    data = '{}'.format(path_value)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
