# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest77512(request: Request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    kind = 'json' if str(profile_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = profile_value
            data = parsed
        case _:
            data = profile_value
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return {"updated": True}
