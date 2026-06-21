# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest29765(request: Request):
    upload_name = (await request.form()).get('upload', '')
    db.execute('SELECT * FROM users WHERE id = ' + str(upload_name))
    return {"updated": True}
