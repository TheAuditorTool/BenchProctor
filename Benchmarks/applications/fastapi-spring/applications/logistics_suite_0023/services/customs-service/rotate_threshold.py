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


@router.post("/rotate_threshold")
async def rotate_threshold(request: Request):
    caption = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    parcel = RequestPayload(caption).value
    parsed = json.loads(parcel)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
