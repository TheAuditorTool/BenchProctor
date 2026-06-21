# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form


async def BenchmarkTest07874(request: Request, field: str = Form('')):
    field_value = field
    kind = 'json' if str(field_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = field_value
            data = parsed
        case _:
            data = field_value
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
