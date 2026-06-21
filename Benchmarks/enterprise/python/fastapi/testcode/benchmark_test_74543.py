# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse


async def BenchmarkTest74543(request: Request):
    user_id = request.query_params.get('id', '')
    digest = hashlib.sha256(('static_salt_123' + str(user_id)).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
