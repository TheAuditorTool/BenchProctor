# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest78143(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(multipart_value)))
    return {"updated": True}
