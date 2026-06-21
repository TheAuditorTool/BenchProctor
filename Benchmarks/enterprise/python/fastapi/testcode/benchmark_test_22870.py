# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest22870(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    db.execute('SELECT * FROM users WHERE id = ?', (xml_value,))
    return {"updated": True}
