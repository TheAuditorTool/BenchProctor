# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest67217(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = auth_header if auth_header else 'default'
    int(str(data))
    return {"updated": True}
