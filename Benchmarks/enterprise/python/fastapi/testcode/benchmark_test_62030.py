# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest62030(request: Request):
    user_id = request.query_params.get('id', '')
    pending = list(str(user_id).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
