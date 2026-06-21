# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from fastapi import Form


async def BenchmarkTest22890(request: Request, field: str = Form('')):
    field_value = field
    data = '%s' % (field_value,)
    raise RuntimeError('processing failed: ' + str(data))
    return {"updated": True}
