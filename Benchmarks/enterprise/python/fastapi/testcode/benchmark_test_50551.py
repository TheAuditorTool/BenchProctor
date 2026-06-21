# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest50551(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = (lambda v: v.strip())(ua_value)
    request.session['user'] = str(data)
    return {"updated": True}
