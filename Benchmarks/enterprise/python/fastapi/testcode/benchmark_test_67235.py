# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from app_runtime import db


async def BenchmarkTest67235(request: Request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    requests.post('http://api.prod.internal/data', data=str(profile_value))
    return {"updated": True}
