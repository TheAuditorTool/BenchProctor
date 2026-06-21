# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest26078(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = (lambda v: v.strip())(auth_header)
    request.session['user'] = str(data)
    return {"updated": True}
