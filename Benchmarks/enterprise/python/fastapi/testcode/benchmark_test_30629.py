# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest30629(request: Request):
    path_value = request.path_params.get('id', '')
    data = '%s' % (path_value,)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
