# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form
from app_runtime import auth_check


async def BenchmarkTest53479(request: Request, field: str = Form('')):
    field_value = field
    kind = 'json' if str(field_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = field_value
            data = parsed
        case _:
            data = field_value
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
