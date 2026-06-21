# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest04870(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    kind = 'json' if str(raw_body).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = raw_body
            data = parsed
        case _:
            data = raw_body
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
