# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest27736(request: Request):
    origin_value = request.headers.get('origin', '')
    data = str(origin_value).replace('\x00', '')
    db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return {"updated": True}
