# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest02443(request: Request):
    upload_name = (await request.form()).get('upload', '')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(upload_name),))
    return {"updated": True}
