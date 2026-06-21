# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
from app_runtime import db


def normalise_input(value):
    return value.strip()

async def BenchmarkTest52710(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = normalise_input(multipart_value)
    if not re.fullmatch('^[\\w\\s.{}\\[\\]:_$\'\\"|=-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    db.users.find({'$where': "this.username == '" + str(processed) + "'"})
    return {"updated": True}
