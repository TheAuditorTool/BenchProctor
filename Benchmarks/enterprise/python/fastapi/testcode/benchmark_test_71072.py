# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest71072(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value}'
    request.session['user'] = str(data)
    return {"updated": True}
