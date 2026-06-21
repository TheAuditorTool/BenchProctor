# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest41952(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data, _sep, _rest = str(header_value).partition('\x00')
    request.session['data'] = str(data)
    return {"updated": True}
