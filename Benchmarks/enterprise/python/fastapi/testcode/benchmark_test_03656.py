# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


def to_text(value):
    return str(value).strip()

async def BenchmarkTest03656(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = to_text(upload_name)
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return {"updated": True}
