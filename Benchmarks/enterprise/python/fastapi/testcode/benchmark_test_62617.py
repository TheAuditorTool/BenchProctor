# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest62617(request: Request):
    auth_header = request.headers.get('authorization', '')
    reader = make_reader(auth_header)
    data = reader()
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    db.users.find({'$where': "this.username == '" + str(processed) + "'"})
    return {"updated": True}
