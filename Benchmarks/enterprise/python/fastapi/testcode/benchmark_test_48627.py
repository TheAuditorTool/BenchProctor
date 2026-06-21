# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest48627(request: Request):
    ua_value = request.headers.get('user-agent', '')
    prefix = ''
    data = prefix + str(ua_value)
    db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return {"updated": True}
