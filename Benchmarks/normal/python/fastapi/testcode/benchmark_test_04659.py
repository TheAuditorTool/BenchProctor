# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest04659(request: Request):
    auth_header = request.headers.get('authorization', '')
    kind = 'json' if str(auth_header).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = auth_header
            data = parsed
        case _:
            data = auth_header
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
