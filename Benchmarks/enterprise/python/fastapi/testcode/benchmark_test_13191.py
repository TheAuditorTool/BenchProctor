# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest13191(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = FormData(payload=upload_name).payload
    return HTMLResponse('<div>' + str(data) + '</div>')
