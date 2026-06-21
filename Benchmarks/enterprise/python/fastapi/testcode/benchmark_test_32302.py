# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest32302(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(comment_value)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = comment_value
    class UserProfile:
        def __init__(self):
            self.name = ''
            self.is_admin = False
    parts = str(processed).split('=', 1)
    profile = UserProfile()
    if len(parts) == 2:
        setattr(profile, parts[0], parts[1])
    return JSONResponse({'is_admin': profile.is_admin}, status_code=200)
