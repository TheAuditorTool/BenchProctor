# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest66278(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = xml_value if xml_value else 'default'
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return {"updated": True}
