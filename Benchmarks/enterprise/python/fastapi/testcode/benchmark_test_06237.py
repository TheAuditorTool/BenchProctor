# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest06237(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(multipart_value),))
    return {"updated": True}
