# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest67153(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = f'{xml_value}'
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(data),))
    return {"updated": True}
