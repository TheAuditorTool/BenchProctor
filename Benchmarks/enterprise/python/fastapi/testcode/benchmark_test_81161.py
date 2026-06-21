# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest81161(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value:.200s}'
    db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return {"updated": True}
