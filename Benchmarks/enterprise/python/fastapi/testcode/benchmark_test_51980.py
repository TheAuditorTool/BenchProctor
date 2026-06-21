# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest51980(request: Request):
    user_id = request.query_params.get('id', '')
    data = '{}'.format(user_id)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
