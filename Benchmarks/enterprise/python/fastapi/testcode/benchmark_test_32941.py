# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest32941(request: Request):
    upload_name = (await request.form()).get('upload', '')
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return {"updated": True}
