# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest06404(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = f'{ua_value}'
    request.session['user'] = str(data)
    return {"updated": True}
