# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest01126(request: Request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    kind = 'json' if str(profile_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = profile_value
            data = parsed
        case _:
            data = profile_value
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
