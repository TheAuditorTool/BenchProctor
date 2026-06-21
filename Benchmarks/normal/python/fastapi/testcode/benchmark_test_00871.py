# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import HTMLResponse
import unicodedata


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest00871(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = coalesce_blank(env_value)
    normalized = unicodedata.normalize('NFKC', str(data))
    return HTMLResponse('<p>' + normalized + '</p>')
