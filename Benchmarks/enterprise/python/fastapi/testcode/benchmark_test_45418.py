# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest45418(request: Request):
    path_value = request.path_params.get('id', '')
    result = 100 / int(str(path_value))
    return {"updated": True}
