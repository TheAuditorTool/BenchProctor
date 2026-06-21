# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest30111(request: Request):
    auth_header = request.headers.get('authorization', '')
    def normalize(value):
        return value.strip()
    data = normalize(auth_header)
    class UserProfile:
        def __init__(self):
            self.name = ''
            self.is_admin = False
    parts = str(data).split('=', 1)
    profile = UserProfile()
    if len(parts) == 2:
        setattr(profile, parts[0], parts[1])
    return JSONResponse({'is_admin': profile.is_admin}, status_code=200)
