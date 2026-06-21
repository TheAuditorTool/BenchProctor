# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
from starlette.responses import RedirectResponse
import urllib.parse


async def BenchmarkTest04205(request: Request):
    user_id = request.query_params.get('id', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(user_id)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = user_id
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return RedirectResponse(url=target)
