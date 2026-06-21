# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest00054(request: Request):
    origin_value = request.headers.get('origin', '')
    db.users.find({'$where': "this.username == '" + str(origin_value) + "'"})
    return {"updated": True}
