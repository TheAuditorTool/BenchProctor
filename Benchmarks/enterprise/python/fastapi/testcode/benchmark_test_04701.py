# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
import os
import ast


async def BenchmarkTest04701(request: Request):
    origin_value = request.headers.get('origin', '')
    try:
        data = str(ast.literal_eval(origin_value))
    except (ValueError, SyntaxError):
        data = origin_value
    if os.environ.get("APP_ENV", "production") != "test":
        return RedirectResponse(url=str(data))
    return {"updated": True}
