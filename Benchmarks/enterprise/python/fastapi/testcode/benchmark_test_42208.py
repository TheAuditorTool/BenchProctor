# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest42208(request: Request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    reader = make_reader(profile_value)
    data = reader()
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
