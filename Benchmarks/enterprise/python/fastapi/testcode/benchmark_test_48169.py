# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest48169(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = f'{upload_name:.200s}'
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
