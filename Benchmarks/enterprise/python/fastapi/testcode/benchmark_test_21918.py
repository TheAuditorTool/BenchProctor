# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest21918(request: Request):
    origin_value = request.headers.get('origin', '')
    reader = make_reader(origin_value)
    data = reader()
    return RedirectResponse(url=str(data))
