# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest72436(request: Request):
    user_id = request.query_params.get('id', '')
    parts = []
    for token in str(user_id).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    result = 100 / int(str(data))
    return {"updated": True}
