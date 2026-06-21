# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import markdown
import bleach


async def BenchmarkTest74080(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '{}'.format(referer_value)
    processed = bleach.clean(markdown.markdown(data))
    return HTMLResponse('<div>' + str(processed) + '</div>')
