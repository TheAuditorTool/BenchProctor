# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest43656(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = RequestPayload(multipart_value).value
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(data),))
    return JSONResponse({'record': str(record)}, status_code=200)
