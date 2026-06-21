# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote


async def BenchmarkTest23030(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
