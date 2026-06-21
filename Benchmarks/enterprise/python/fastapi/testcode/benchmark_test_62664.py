# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest62664(request: Request):
    upload_name = (await request.form()).get('upload', '')
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(upload_name),))
    return {"updated": True}
