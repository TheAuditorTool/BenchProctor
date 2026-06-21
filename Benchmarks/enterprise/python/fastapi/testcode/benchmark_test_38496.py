# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest38496(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return {"updated": True}
