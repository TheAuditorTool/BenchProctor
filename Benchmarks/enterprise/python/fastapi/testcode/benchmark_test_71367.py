# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from starlette.responses import JSONResponse
from app_runtime import db


@dataclass
class FormData:
    payload: str

async def BenchmarkTest71367(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = FormData(payload=db_value).payload
    try:
        processed = max(0, min(int(data), 2147483647))
    except (TypeError, ValueError):
        return JSONResponse({'error': 'invalid integer'}, status_code=400)
    requested = int(processed)
    allocated = min(requested + 1, 2147483647)
    return JSONResponse({'allocated': allocated}, status_code=200)
