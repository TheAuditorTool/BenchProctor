# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest78342(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    reader = make_reader(multipart_value)
    data = reader()
    return RedirectResponse(url=str(data))
