# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse


def ensure_str(value):
    return str(value)

async def BenchmarkTest48033(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = ensure_str(auth_header)
    processed = data[:64]
    return RedirectResponse(url=str(processed))
