# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


async def BenchmarkTest00314(request: Request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    parts = str(profile_value).split(',')
    data = ','.join(parts)
    os.unlink('/var/app/data/' + str(data))
    return {"updated": True}
