# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest06121(request: Request):
    user_id = request.query_params.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
