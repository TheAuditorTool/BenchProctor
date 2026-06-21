# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import json
from app_runtime import db


async def BenchmarkTest79571(request: Request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    try:
        data = json.loads(profile_value).get('value', profile_value)
    except (json.JSONDecodeError, AttributeError):
        data = profile_value
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
