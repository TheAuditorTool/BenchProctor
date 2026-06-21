# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest22682(request: Request):
    user_id = request.query_params.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    request.session['data'] = str(data)
    return {"updated": True}
