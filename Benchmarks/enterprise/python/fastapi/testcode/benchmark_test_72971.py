# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest72971(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = auth_header if auth_header else 'default'
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
