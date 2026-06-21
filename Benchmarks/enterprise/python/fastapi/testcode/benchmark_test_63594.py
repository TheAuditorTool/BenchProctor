# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from urllib.parse import unquote
from starlette.responses import JSONResponse


async def BenchmarkTest63594(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    digest = str(data).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
