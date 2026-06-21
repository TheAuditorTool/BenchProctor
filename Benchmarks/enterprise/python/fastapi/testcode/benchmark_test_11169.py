# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def ensure_str(value):
    return str(value)

async def BenchmarkTest11169(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = ensure_str(auth_header)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
