# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest41569(request: Request):
    host_value = request.headers.get('host', '')
    data = f'{host_value:.200s}'
    request.session['data'] = str(data)
    return {"updated": True}
