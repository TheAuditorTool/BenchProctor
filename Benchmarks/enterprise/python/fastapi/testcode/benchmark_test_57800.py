# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest57800(request: Request):
    user_id = request.query_params.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    request.session['data'] = str(data)
    return {"updated": True}
