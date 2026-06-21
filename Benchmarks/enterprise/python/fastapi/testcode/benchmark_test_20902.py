# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


def relay_value(value):
    return value

async def BenchmarkTest20902(request: Request):
    user_id = request.query_params.get('id', '')
    data = relay_value(user_id)
    db.execute('SELECT * FROM "' + str(data).replace('"', '""') + '"')
    return {"updated": True}
