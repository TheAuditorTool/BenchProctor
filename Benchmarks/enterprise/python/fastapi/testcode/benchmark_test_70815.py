# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest70815(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value:.200s}'
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
