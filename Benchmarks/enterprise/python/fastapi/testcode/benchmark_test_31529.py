# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest31529(request: Request, field: str = Form('')):
    field_value = field
    class UserProfile:
        def __init__(self):
            self.name = ''
            self.is_admin = False
    parts = str(field_value).split('=', 1)
    profile = UserProfile()
    if len(parts) == 2:
        setattr(profile, parts[0], parts[1])
    return JSONResponse({'is_admin': profile.is_admin}, status_code=200)
