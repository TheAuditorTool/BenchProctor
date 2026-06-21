# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest69548(request: Request):
    host_value = request.headers.get('host', '')
    data = str(host_value).replace('\x00', '')
    db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return {"updated": True}
