# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest30087(request: Request):
    user_id = request.query_params.get('id', '')
    data = '%s' % (user_id,)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
