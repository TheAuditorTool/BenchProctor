# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from pydantic import BaseModel
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse
import unicodedata


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest70461(request: Request, req: UserInput):
    json_value = req.payload
    data = '%s' % (json_value,)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    normalized = unicodedata.normalize('NFKC', str(processed))
    return HTMLResponse('<p>' + normalized + '</p>')
