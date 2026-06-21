# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest15644(request: Request):
    user_id = request.query_params.get('id', '')
    data = '%s' % str(user_id)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
