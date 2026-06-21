# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote


async def BenchmarkTest11236(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
