# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest75870(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = f'{upload_name}'
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return {"updated": True}
