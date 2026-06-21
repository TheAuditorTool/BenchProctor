# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib


async def BenchmarkTest54204(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return {"updated": True}
