# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


async def BenchmarkTest74444(request: Request, field: str = Form('')):
    field_value = field
    kind = 'json' if str(field_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = field_value
            data = parsed
        case _:
            data = field_value
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
