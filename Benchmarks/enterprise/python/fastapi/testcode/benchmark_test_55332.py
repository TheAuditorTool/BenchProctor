# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import re


async def BenchmarkTest55332(request: Request):
    user_id = request.query_params.get('id', '')
    if re.search('[a-zA-Z0-9_-]+', str(user_id)):
        return JSONResponse({'validated': str(user_id)}, status_code=200)
    return {"updated": True}
