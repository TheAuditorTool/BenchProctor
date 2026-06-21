# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest35092(request: Request):
    ua_value = request.headers.get('user-agent', '')
    kind = 'json' if str(ua_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = ua_value
            data = parsed
        case _:
            data = ua_value
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
