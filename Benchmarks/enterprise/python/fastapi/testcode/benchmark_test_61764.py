# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import re
import json
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest61764(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return {"updated": True}
