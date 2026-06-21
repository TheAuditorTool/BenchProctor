# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest06548(request: Request):
    user_id = request.query_params.get('id', '')
    pending = list(str(user_id).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
