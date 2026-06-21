# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest69808(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    reader = make_reader(header_value)
    data = reader()
    return RedirectResponse(url=str(data))
