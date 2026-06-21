# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest35016(request: Request):
    user_id = request.query_params.get('id', '')
    data = '%s' % (user_id,)
    int(str(data))
    return {"updated": True}
