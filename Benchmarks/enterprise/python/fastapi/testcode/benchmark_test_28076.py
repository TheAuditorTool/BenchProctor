# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest28076(request: Request):
    user_id = request.query_params.get('id', '')
    pending = list(str(user_id).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    os.unlink('/var/app/data/' + str(data))
    return {"updated": True}
