# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


async def BenchmarkTest20024(request: Request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    data = f'{profile_value:.200s}'
    os.unlink('/var/app/data/' + str(data))
    return {"updated": True}
