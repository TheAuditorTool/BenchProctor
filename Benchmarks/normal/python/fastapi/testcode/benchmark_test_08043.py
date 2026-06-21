# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


def ensure_str(value):
    return str(value)

async def BenchmarkTest08043(request: Request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    data = ensure_str(profile_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
