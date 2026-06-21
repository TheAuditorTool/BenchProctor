# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse


async def BenchmarkTest05653(request: Request):
    auth_header = request.headers.get('authorization', '')
    return RedirectResponse(url=str(auth_header))
