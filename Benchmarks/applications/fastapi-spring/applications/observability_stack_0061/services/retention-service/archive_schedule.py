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


@router.post("/archive_schedule")
async def archive_schedule(request: Request):
    headline = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    cohort = RequestPayload(headline).value
    parsed = json.loads(cohort)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
