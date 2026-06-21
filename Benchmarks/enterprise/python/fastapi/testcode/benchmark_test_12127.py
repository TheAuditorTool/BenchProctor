# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest12127(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = bytes.fromhex(auth_header).decode('utf-8', 'ignore')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
