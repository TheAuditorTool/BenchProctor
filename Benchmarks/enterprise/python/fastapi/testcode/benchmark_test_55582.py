# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import HTMLResponse
import unicodedata


async def BenchmarkTest55582(request: Request, field: str = Form('')):
    field_value = field
    data = '%s' % (field_value,)
    normalized = unicodedata.normalize('NFKC', str(data))
    return HTMLResponse('<p>' + normalized + '</p>')
