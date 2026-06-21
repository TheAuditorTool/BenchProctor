# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
from app_runtime import db


async def BenchmarkTest26654(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    return RedirectResponse(url=str(db_value))
