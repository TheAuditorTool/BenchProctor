# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest64466(request: Request):
    user_id = request.query_params.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
