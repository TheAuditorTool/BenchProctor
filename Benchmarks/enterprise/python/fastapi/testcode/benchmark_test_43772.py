# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest43772(request: Request):
    path_value = request.path_params.get('id', '')
    reader = make_reader(path_value)
    data = reader()
    raise RuntimeError('processing failed: ' + str(data))
    return {"updated": True}
