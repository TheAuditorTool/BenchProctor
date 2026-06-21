# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest20915(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '%s' % str(auth_header)
    request.session['user'] = str(data)
    return {"updated": True}
