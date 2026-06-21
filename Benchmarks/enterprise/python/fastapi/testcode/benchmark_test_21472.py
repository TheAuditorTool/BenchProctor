# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os
from starlette.responses import HTMLResponse


async def BenchmarkTest21472(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    return HTMLResponse('<script src="' + str(data) + '"></script>')
