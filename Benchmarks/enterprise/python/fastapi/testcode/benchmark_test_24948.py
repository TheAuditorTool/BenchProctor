# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest24948(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = f'{header_value:.200s}'
    request.session['data'] = str(data)
    return {"updated": True}
