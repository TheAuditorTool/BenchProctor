# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from types import SimpleNamespace


async def BenchmarkTest80948(request: Request):
    host_value = request.headers.get('host', '')
    ns = SimpleNamespace(payload=host_value)
    data = getattr(ns, 'payload')
    allowed_fields = {'name', 'email', 'bio'}
    if str(data).split('=', 1)[0] not in allowed_fields:
        return JSONResponse({'error': 'field not allowed'}, status_code=400)
    processed = data
    class UserProfile:
        def __init__(self):
            self.name = ''
            self.is_admin = False
    parts = str(processed).split('=', 1)
    profile = UserProfile()
    if len(parts) == 2:
        setattr(profile, parts[0], parts[1])
    return JSONResponse({'is_admin': profile.is_admin}, status_code=200)
