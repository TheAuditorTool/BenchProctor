# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest45038(request: Request):
    ua_value = request.headers.get('user-agent', '')
    parts = []
    for token in str(ua_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
