# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
from app_runtime import db


async def BenchmarkTest77921(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return {"updated": True}
