# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest54245(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    def normalize(value):
        return value.strip()
    data = normalize(header_value)
    db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return {"updated": True}
