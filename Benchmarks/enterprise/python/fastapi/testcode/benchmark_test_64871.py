# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest64871(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = xml_value.decode('utf-8', 'ignore') if isinstance(xml_value, bytes) else xml_value
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return {"updated": True}
