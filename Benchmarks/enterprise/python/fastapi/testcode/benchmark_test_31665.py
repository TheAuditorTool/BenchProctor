# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest31665(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = f'{auth_header:.200s}'
    request.session['user'] = str(data)
    return {"updated": True}
