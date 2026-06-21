# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest69761(request: Request):
    user_id = request.query_params.get('id', '')
    data = f'{user_id}'
    request.session['user'] = str(data)
    return {"updated": True}
