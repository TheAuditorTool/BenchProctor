# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest01554(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    reader = make_reader(multipart_value)
    data = reader()
    secret = db.fetch_one('SELECT secret FROM vault WHERE owner = ?', (str(data),))
    return JSONResponse({'secret': str(secret)}, status_code=200)
