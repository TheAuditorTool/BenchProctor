# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest61575(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    prefix = ''
    data = prefix + str(multipart_value)
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
