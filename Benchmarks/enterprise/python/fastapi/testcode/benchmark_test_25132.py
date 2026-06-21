# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def relay_value(value):
    return value

async def BenchmarkTest25132(request: Request):
    user_id = request.query_params.get('id', '')
    data = relay_value(user_id)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
