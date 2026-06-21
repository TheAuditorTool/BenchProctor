# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest07854(request: Request):
    ua_value = request.headers.get('user-agent', '')
    kind = 'json' if str(ua_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = ua_value
            data = parsed
        case _:
            data = ua_value
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
