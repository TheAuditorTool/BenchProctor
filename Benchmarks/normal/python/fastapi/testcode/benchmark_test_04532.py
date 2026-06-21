# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest04532(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = (lambda v: v.strip())(upload_name)
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
