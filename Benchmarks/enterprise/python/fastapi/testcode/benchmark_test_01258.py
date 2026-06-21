# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest01258(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = f'{ua_value:.200s}'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
