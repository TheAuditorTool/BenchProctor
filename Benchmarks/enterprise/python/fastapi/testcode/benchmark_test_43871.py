# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest43871(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = (lambda v: v.strip())(auth_header)
    request.session['data'] = str(data)
    return {"updated": True}
