# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import json
from app_runtime import db


async def BenchmarkTest45938(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    raise RuntimeError('processing failed: ' + str(data))
    return {"updated": True}
