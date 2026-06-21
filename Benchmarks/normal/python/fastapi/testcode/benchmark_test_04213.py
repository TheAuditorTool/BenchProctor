# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest04213(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(xml_value)))
    return {"updated": True}
