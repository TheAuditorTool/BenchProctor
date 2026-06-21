# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from app_runtime import db


async def BenchmarkTest37573(request: Request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    kind = 'json' if str(profile_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = profile_value
            data = parsed
        case _:
            data = profile_value
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
