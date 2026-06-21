# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from app_runtime import db


async def BenchmarkTest19825(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = unquote(multipart_value)
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(data),))
    return {"updated": True}
