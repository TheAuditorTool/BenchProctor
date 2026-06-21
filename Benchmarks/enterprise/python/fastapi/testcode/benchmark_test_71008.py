# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest71008(request: Request):
    upload_name = (await request.form()).get('upload', '')
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(upload_name),))
    return JSONResponse({'record': str(record)}, status_code=200)
