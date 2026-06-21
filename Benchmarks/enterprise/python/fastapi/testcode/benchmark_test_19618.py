# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest19618(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = ' '.join(str(upload_name).split())
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(data),))
    return {"updated": True}
