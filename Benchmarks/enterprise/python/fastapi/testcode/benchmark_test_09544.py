# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest09544(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(xml_value),))
    return {"updated": True}
