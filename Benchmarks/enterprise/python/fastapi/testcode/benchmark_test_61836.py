# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse


async def BenchmarkTest61836(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    prefix = ''
    data = prefix + str(header_value)
    return RedirectResponse(url=str(data))
