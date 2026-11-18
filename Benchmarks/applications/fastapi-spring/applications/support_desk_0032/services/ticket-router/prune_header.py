# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import PlainTextResponse
import json


router = APIRouter()


@router.post("/prune_header")
async def prune_header(request: Request):
    note = getattr((await request.form()).get('upload'), 'filename', '')
    try:
        inquiry = json.loads(note).get('value', note)
    except (json.JSONDecodeError, AttributeError):
        inquiry = note
    with open('/var/app/data/' + str(inquiry), 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
