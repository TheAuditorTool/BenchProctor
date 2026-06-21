# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from fastapi import Form


async def BenchmarkTest59015(request: Request, field: str = Form('')):
    field_value = field
    raise RuntimeError('processing failed: ' + str(field_value))
    return {"updated": True}
