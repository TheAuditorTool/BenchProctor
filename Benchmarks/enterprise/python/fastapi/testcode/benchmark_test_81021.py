# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest81021(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = f'{ua_value:.200s}'
    request.session['user'] = str(data)
    return {"updated": True}
