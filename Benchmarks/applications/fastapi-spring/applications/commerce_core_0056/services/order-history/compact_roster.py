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


@router.post("/compact_roster")
async def compact_roster(request: Request):
    citation = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    backorder = RequestPayload(citation).value
    parsed = json.loads(backorder)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
