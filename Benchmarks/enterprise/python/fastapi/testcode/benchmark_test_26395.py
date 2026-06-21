# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse


async def BenchmarkTest26395(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = str(header_value).replace('\x00', '')
    return RedirectResponse(url=str(data))
