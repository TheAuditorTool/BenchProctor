# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest48203(request: Request):
    user_id = request.query_params.get('id', '')
    data = '%s' % str(user_id)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
