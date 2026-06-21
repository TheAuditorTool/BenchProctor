# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest15157(request: Request):
    ua_value = request.headers.get('user-agent', '')
    kind = 'json' if str(ua_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = ua_value
            data = parsed
        case _:
            data = ua_value
    result = 100 / int(str(data))
    return {"updated": True}
