# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


async def BenchmarkTest60480(request: Request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    data, _sep, _rest = str(profile_value).partition('\x00')
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'w') as fh:
        fh.write('data')
    return {"updated": True}
