# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse


async def BenchmarkTest43652(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = f'{raw_body}'
    return RedirectResponse(url=str(data))
