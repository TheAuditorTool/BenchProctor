# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


def normalise_input(value):
    return value.strip()

async def BenchmarkTest03768(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = normalise_input(header_value)
    db.execute('UPDATE users SET name = ?', (str(data),))
    return {"updated": True}
