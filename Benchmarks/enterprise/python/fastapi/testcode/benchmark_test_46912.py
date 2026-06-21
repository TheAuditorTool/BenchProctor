# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest46912(request: Request):
    path_value = request.path_params.get('id', '')
    parts = []
    for token in str(path_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    eval(str(data))
    return {"updated": True}
