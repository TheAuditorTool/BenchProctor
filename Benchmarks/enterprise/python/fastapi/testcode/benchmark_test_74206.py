# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest74206(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '{}'.format(auth_header)
    request.session['data'] = str(data)
    return {"updated": True}
