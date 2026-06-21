# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from types import SimpleNamespace


async def BenchmarkTest52363(request: Request):
    user_id = request.query_params.get('id', '')
    ns = SimpleNamespace(payload=user_id)
    data = getattr(ns, 'payload')
    class UserProfile:
        def __init__(self):
            self.name = ''
            self.is_admin = False
    parts = str(data).split('=', 1)
    profile = UserProfile()
    if len(parts) == 2:
        setattr(profile, parts[0], parts[1])
    return JSONResponse({'is_admin': profile.is_admin}, status_code=200)
