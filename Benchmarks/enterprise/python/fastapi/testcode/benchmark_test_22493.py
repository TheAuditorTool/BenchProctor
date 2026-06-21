# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest22493(request: Request):
    user_id = request.query_params.get('id', '')
    data = '%s' % str(user_id)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
