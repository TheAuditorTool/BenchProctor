# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest49574(request: Request):
    user_id = request.query_params.get('id', '')
    data = f'{user_id:.200s}'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
