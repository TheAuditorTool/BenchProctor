# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote


async def BenchmarkTest00790(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    eval(str(data))
    return {"updated": True}
