# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse


async def BenchmarkTest45924(request: Request):
    user_id = request.query_params.get('id', '')
    digest = str(user_id).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
