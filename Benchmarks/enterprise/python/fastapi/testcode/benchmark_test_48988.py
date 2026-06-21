# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from app_runtime import db


async def BenchmarkTest48988(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = unquote(multipart_value)
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return {"updated": True}
