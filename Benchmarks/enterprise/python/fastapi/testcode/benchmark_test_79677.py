# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from app_runtime import db


def ensure_str(value):
    return str(value)

async def BenchmarkTest79677(request: Request, field: str = Form('')):
    field_value = field
    data = ensure_str(field_value)
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
