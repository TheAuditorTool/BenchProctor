# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest36827(request: Request):
    auth_header = request.headers.get('authorization', '')
    request.session['data'] = str(auth_header)
    return {"updated": True}
