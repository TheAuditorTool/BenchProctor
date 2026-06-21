# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest29343(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = ' '.join(str(auth_header).split())
    request.session['user'] = str(data)
    return {"updated": True}
