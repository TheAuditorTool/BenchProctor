# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest08399(request: Request):
    upload_name = (await request.form()).get('upload', '')
    if upload_name:
        data = upload_name
    else:
        data = ''
    db.execute('SELECT * FROM users WHERE id = :id', {'id': data})
    return {"updated": True}
