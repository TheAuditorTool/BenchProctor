# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest23511(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value:.200s}'
    request.session['data'] = str(data)
    return {"updated": True}
