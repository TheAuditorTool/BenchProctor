# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest27203(request: Request):
    host_value = request.headers.get('host', '')
    data = f'{host_value:.200s}'
    request.session['user'] = str(data)
    return {"updated": True}
