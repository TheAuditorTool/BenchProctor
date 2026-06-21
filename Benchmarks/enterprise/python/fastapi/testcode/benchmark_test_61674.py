# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def normalise_input(value):
    return value.strip()

async def BenchmarkTest61674(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = normalise_input(cookie_value)
    request.session['data'] = str(data)
    return {"updated": True}
