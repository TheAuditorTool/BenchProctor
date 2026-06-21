# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest81172(request: Request):
    upload_name = (await request.form()).get('upload', '')
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(upload_name)))
    return {"updated": True}
