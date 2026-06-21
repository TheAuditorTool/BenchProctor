# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest26497(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    kind = 'json' if str(header_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = header_value
            data = parsed
        case _:
            data = header_value
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
