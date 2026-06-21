# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import markdown
import bleach


def normalise_input(value):
    return value.strip()

async def BenchmarkTest58140(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = normalise_input(ua_value)
    processed = bleach.clean(markdown.markdown(data))
    return HTMLResponse('<div>' + str(processed) + '</div>')
