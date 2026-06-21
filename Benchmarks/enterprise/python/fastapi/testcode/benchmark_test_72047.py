# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form


async def BenchmarkTest72047(request: Request, field: str = Form('')):
    field_value = field
    kind = 'json' if str(field_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = field_value
            data = parsed
        case _:
            data = field_value
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
