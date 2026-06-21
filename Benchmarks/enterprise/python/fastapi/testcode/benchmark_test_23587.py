# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os
from starlette.responses import HTMLResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest23587(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    return HTMLResponse('<script src="' + str(data) + '"></script>')
