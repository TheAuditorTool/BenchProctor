# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest50533(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = coalesce_blank(upload_name)
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
