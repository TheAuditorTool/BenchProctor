# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest32541(request: Request):
    user_id = request.query_params.get('id', '')
    data = str(user_id).replace('\x00', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
