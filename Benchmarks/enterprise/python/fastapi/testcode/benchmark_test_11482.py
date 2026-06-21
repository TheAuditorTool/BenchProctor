# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest11482(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = f'{auth_header:.200s}'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
