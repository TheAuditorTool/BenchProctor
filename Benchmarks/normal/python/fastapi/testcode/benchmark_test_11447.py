# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest11447(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = default_blank(auth_header)
    processed = data[:64]
    return RedirectResponse(url=str(processed))
