# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest28433(request: Request):
    user_id = request.query_params.get('id', '')
    data = '{}'.format(user_id)
    db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return {"updated": True}
