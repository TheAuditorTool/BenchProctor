# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


async def BenchmarkTest14946(request: Request, field: str = Form('')):
    field_value = field
    data = '%s' % (field_value,)
    request.session['user'] = str(data)
    return {"updated": True}
