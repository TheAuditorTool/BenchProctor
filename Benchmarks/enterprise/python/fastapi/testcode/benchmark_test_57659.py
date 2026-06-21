# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest57659(request: Request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(profile_value))
    return {"updated": True}
