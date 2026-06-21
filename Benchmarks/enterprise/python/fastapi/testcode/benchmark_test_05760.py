# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest05760(request: Request):
    path_value = request.path_params.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
