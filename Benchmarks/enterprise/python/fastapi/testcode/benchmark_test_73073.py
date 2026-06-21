# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest73073(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = str(header_value).replace('\x00', '')
    request.session['user'] = str(data)
    return {"updated": True}
