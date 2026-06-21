# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from starlette.responses import JSONResponse
import re


async def BenchmarkTest40261(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return JSONResponse({'validated': str(data)}, status_code=200)
    return {"updated": True}
