# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import json


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

router = APIRouter()


@router.post("/collect_checkpoint")
async def collect_checkpoint(request: Request):
    synopsis = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    handshake = RequestPayload(synopsis).value
    parsed = json.loads(handshake)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
