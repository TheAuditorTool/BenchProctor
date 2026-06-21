# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest62979(request: Request):
    path_value = request.path_params.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    eval(str(data))
    return {"updated": True}
