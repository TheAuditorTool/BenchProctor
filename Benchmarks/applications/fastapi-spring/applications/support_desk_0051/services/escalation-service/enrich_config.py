# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import yaml
from starlette.responses import JSONResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

router = APIRouter()


@router.post("/enrich_config/{id}")
async def enrich_config(request: Request, id: str):
    preface = request.path_params.get('id', '')
    grievance = RequestPayload(preface).value
    parsed = yaml.safe_load(grievance)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
