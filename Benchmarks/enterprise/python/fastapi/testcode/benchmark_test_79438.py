# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest79438(request: Request):
    user_id = request.query_params.get('id', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(user_id))
    return {"updated": True}
