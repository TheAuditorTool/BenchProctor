# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def to_text(value):
    return str(value).strip()

async def BenchmarkTest54842(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = to_text(cookie_value)
    processed = data[:64]
    request.session['data'] = str(processed)
    return {"updated": True}
