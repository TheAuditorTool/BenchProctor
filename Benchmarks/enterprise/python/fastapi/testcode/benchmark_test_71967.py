# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest71967(request: Request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    data, _sep, _rest = str(profile_value).partition('\x00')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
