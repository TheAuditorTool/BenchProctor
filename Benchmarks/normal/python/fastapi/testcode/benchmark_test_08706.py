# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest08706(request: Request):
    user_id = request.query_params.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
