# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse


async def BenchmarkTest76890(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    return RedirectResponse(url=str(header_value))
