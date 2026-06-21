# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest17482(request: Request):
    upload_name = (await request.form()).get('upload', '')
    reader = make_reader(upload_name)
    data = reader()
    processed = html.escape(data)
    return HTMLResponse('<img src="' + str(processed) + '">')
