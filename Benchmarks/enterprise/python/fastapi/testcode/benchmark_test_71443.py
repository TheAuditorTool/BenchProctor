# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest71443(request: Request):
    auth_header = request.headers.get('authorization', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
