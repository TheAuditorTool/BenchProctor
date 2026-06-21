# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest38914(request: Request):
    user_id = request.query_params.get('id', '')
    db.users.find({'$where': "this.username == '" + str(user_id) + "'"})
    return {"updated": True}
