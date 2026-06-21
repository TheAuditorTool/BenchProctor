# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import JSONResponse
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest04221(request: Request, field: str = Form('')):
    field_value = field
    reader = make_reader(field_value)
    data = reader()
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(data),))
    return JSONResponse({'record': str(record)}, status_code=200)
