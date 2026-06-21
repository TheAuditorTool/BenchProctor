# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse


async def BenchmarkTest01363(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(xml_value)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = xml_value
    class UserProfile:
        def __init__(self):
            self.name = ''
            self.is_admin = False
    parts = str(processed).split('=', 1)
    profile = UserProfile()
    if len(parts) == 2:
        setattr(profile, parts[0], parts[1])
    return JSONResponse({'is_admin': profile.is_admin}, status_code=200)
