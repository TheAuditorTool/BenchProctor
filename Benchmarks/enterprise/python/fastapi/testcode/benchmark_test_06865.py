# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest06865(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = '%s' % str(header_value)
    request.session['data'] = str(data)
    return {"updated": True}
