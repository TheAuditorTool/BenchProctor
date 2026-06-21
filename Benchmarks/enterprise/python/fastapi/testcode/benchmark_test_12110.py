# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest12110(request: Request):
    user_id = request.query_params.get('id', '')
    data = '%s' % str(user_id)
    request.session['user'] = str(data)
    return {"updated": True}
