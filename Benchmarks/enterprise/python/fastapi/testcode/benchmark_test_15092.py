# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import os


def to_text(value):
    return str(value).strip()

async def BenchmarkTest15092(request: Request):
    path_value = request.path_params.get('id', '')
    data = to_text(path_value)
    if os.environ.get("APP_ENV", "production") != "test":
        return HTMLResponse('<div>' + str(data) + '</div>')
    return {"updated": True}
