# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from fastapi import Form
from app_runtime import db


async def BenchmarkTest12758(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    db.execute('UPDATE users SET name = ?', (str(data),))
    return {"updated": True}
