# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from app_runtime import db


async def BenchmarkTest33902(request: Request, field: str = Form('')):
    field_value = field
    db.execute('DELETE FROM accounts WHERE id = ?', (str(field_value),))
    return {"updated": True}
