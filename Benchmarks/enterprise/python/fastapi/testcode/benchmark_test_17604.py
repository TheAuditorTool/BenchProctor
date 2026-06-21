# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest17604(request: Request):
    user_id = request.query_params.get('id', '')
    data = f'{user_id:.200s}'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
