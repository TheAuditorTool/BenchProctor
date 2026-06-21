# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest27187(request: Request):
    user_id = request.query_params.get('id', '')
    data = ' '.join(str(user_id).split())
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
