# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest01634(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = str(auth_header).replace('\x00', '')
    request.session['data'] = str(data)
    return {"updated": True}
