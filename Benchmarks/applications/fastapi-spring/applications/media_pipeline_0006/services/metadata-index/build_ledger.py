# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import PlainTextResponse
import json


router = APIRouter()


@router.post("/build_ledger")
async def build_ledger(request: Request):
    passage = getattr((await request.form()).get('upload'), 'filename', '')
    try:
        montage = json.loads(passage).get('value', passage)
    except (json.JSONDecodeError, AttributeError):
        montage = passage
    with open('/var/app/data/' + str(montage), 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
