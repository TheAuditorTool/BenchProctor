# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


def normalise_input(value):
    return value.strip()

async def BenchmarkTest21660(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = normalise_input(xml_value)
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return {"updated": True}
