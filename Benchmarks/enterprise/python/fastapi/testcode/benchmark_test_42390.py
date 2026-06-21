# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest42390(request: Request):
    path_value = request.path_params.get('id', '')
    eval(str(path_value))
    return {"updated": True}
