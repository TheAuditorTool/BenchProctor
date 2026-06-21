# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest55112(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    pending = list(str(multipart_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
