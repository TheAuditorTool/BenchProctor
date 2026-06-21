# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from app_runtime import db


async def BenchmarkTest45952(request: Request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    try:
        data = json.loads(profile_value).get('value', profile_value)
    except (json.JSONDecodeError, AttributeError):
        data = profile_value
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
