# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest05553(request: Request):
    user_id = request.query_params.get('id', '')
    data = '%s' % (user_id,)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}
