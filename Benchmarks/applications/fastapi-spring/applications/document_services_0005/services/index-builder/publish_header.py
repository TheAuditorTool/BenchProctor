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


@router.post("/publish_header/{id}")
async def publish_header(request: Request, id: str):
    footnote = request.path_params.get('id', '')
    addendum = RequestPayload(footnote).value
    parsed = yaml.safe_load(addendum)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
