# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest05982(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = header_value if header_value else 'default'
    request.session['data'] = str(data)
    return {"updated": True}
