# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest35875(request: Request):
    user_id = request.query_params.get('id', '')
    data = '%s' % str(user_id)
    result = 100 / int(str(data))
    return {"updated": True}
