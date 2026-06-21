# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest43254(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    prefix = ''
    data = prefix + str(header_value)
    request.session['data'] = str(data)
    return {"updated": True}
