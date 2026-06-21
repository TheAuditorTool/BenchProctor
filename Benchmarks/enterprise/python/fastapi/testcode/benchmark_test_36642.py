# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse


async def BenchmarkTest36642(request: Request):
    user_id = request.query_params.get('id', '')
    data = '%s' % str(user_id)
    digest = str(data).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
