# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest64992(request: Request):
    referer_value = request.headers.get('referer', '')
    kind = 'json' if str(referer_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = referer_value
            data = parsed
        case _:
            data = referer_value
    eval(str(data))
    return {"updated": True}
