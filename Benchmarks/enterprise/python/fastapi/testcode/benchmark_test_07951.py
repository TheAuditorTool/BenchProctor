# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest07951(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = auth_header if auth_header else 'default'
    result = 100 / int(str(data))
    return {"updated": True}
