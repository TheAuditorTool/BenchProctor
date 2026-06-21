# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest07233(request: Request):
    user_id = request.query_params.get('id', '')
    data = ' '.join(str(user_id).split())
    request.session['data'] = str(data)
    return {"updated": True}
