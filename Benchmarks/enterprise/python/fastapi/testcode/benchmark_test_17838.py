# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from app_runtime import db


def normalise_input(value):
    return value.strip()

async def BenchmarkTest17838(request: Request, field: str = Form('')):
    field_value = field
    data = normalise_input(field_value)
    db.execute('UPDATE users SET name = ?', (str(data),))
    return {"updated": True}
