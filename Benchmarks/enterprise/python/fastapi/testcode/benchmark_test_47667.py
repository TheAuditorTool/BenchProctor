# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest47667(request: Request):
    user_id = request.query_params.get('id', '')
    data = (lambda v: v.strip())(user_id)
    request.session['data'] = str(data)
    return {"updated": True}
