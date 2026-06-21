# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest32639(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = FormData(payload=xml_value).payload
    processed = html.escape(data)
    return HTMLResponse('<img src="' + str(processed) + '">')
