# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest67764(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = bytes.fromhex(auth_header).decode('utf-8', 'ignore')
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
