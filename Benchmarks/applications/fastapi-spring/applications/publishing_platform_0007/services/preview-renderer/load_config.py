# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import base64
import pickle


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

router = APIRouter()


@router.post("/load_config")
async def load_config(request: Request):
    remark = (await request.form()).get('multipart_field', '')
    byline = RequestPayload(remark).value
    pickle.loads(base64.b64decode(byline))
    return {"updated": True}
