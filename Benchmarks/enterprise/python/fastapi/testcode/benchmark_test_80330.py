# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def to_text(value):
    return str(value).strip()

async def BenchmarkTest80330(request: Request):
    user_id = request.query_params.get('id', '')
    data = to_text(user_id)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
