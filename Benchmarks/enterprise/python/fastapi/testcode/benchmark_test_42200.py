# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest42200(request: Request):
    path_value = request.path_params.get('id', '')
    parts = []
    for token in str(path_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    result = 100 / int(str(data))
    return {"updated": True}
