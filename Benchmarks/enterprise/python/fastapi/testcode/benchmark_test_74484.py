# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest74484(request: Request):
    auth_header = request.headers.get('authorization', '')
    db.users.find({'$where': "this.username == '" + str(auth_header) + "'"})
    return {"updated": True}
