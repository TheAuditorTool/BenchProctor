# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest33896(request: Request):
    upload_name = (await request.form()).get('upload', '')
    kind = 'json' if str(upload_name).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = upload_name
            data = parsed
        case _:
            data = upload_name
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return {"updated": True}
