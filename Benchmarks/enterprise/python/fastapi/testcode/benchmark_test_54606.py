# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
from fastapi import Form


async def BenchmarkTest54606(request: Request, field: str = Form('')):
    field_value = field
    data = '%s' % str(field_value)
    return RedirectResponse(url=str(data))
