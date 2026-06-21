# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest23725(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = upload_name if upload_name else 'default'
    db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return {"updated": True}
