# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest08694(request: Request):
    user_id = request.query_params.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
