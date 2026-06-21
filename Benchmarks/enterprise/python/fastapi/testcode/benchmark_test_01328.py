# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from starlette.responses import JSONResponse


async def BenchmarkTest01328(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    class UserProfile:
        def __init__(self):
            self.name = ''
            self.is_admin = False
    parts = str(processed).split('=', 1)
    profile = UserProfile()
    if len(parts) == 2:
        setattr(profile, parts[0], parts[1])
    return JSONResponse({'is_admin': profile.is_admin}, status_code=200)
