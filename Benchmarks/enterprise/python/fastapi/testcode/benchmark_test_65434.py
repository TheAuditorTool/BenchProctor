# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest65434(request: Request):
    host_value = request.headers.get('host', '')
    data = '{}'.format(host_value)
    db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return {"updated": True}
