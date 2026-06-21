# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest06045(request: Request, field: str = Form('')):
    field_value = field
    reader = make_reader(field_value)
    data = reader()
    db.execute('UPDATE users SET name = ?', (str(data),))
    return {"updated": True}
