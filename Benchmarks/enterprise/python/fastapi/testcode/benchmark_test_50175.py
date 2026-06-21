# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest50175(request: Request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    data = '%s' % (profile_value,)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
