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


@router.post("/rotate_digest/{id}")
async def rotate_digest(request: Request, id: str):
    excerpt = request.path_params.get('id', '')
    restock = RequestPayload(excerpt).value
    parsed = yaml.safe_load(restock)
    return JSONResponse({'parsed': str(parsed)}, status_code=200)
