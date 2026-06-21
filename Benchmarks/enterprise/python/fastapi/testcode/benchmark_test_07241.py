# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest07241(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    processed = html.escape(data)
    return HTMLResponse('<img src="' + str(processed) + '">')
