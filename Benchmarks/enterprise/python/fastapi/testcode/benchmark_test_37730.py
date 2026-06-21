# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


async def BenchmarkTest37730(request: Request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    if profile_value:
        data = profile_value
    else:
        data = ''
    os.unlink('/var/app/data/' + str(data))
    return {"updated": True}
