# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest27780(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = f'{auth_header}'
    db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return {"updated": True}
