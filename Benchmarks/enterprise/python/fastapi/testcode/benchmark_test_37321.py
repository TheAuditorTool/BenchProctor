# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest37321(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return {"updated": True}
