# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from app_runtime import db


async def BenchmarkTest38106(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value:.200s}'
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return {"updated": True}
