# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest20095(request: Request):
    user_id = request.query_params.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
