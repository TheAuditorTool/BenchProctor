# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
import json


async def BenchmarkTest05567(request: Request):
    upload_name = (await request.form()).get('upload', '')
    try:
        data = json.loads(upload_name).get('value', upload_name)
    except (json.JSONDecodeError, AttributeError):
        data = upload_name
    processed = html.escape(data)
    return HTMLResponse('<img src="' + str(processed) + '">')
