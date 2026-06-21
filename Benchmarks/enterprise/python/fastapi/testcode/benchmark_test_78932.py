# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import markdown
import bleach
from fastapi import Form


async def BenchmarkTest78932(request: Request, field: str = Form('')):
    field_value = field
    data = ' '.join(str(field_value).split())
    processed = bleach.clean(markdown.markdown(data))
    return HTMLResponse('<div>' + str(processed) + '</div>')
