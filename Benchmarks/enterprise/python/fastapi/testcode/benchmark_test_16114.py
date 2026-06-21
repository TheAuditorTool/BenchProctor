# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest16114(request: Request):
    path_value = request.path_params.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    request.session['data'] = str(data)
    return {"updated": True}
