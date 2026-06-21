# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
from fastapi import Form


async def BenchmarkTest15209(request: Request, field: str = Form('')):
    field_value = field
    return RedirectResponse(url=str(field_value))
