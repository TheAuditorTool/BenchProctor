# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest36396(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    reader = make_reader(raw_body)
    data = reader()
    return RedirectResponse(url=str(data))
