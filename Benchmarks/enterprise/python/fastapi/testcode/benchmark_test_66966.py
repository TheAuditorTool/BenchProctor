# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest66966(request: Request):
    user_id = request.query_params.get('id', '')
    data = user_id if user_id else 'default'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
