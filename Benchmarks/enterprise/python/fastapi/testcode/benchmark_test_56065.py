# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest56065(request: Request):
    user_id = request.query_params.get('id', '')
    data = bytes.fromhex(user_id).decode('utf-8', 'ignore')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
