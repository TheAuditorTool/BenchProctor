# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest11273(request: Request):
    user_id = request.query_params.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
