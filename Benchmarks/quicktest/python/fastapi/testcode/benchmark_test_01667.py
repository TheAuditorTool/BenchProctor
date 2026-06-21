# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest01667(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    if header_value:
        data = header_value
    else:
        data = ''
    request.session['user'] = str(data)
    return {"updated": True}
