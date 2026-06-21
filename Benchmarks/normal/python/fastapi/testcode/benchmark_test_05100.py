# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


def normalise_input(value):
    return value.strip()

async def BenchmarkTest05100(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = normalise_input(xml_value)
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(data),))
    value = result['name']
    return JSONResponse({'name': str(value)}, status_code=200)
