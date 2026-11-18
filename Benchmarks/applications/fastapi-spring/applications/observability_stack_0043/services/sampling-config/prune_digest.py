# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import PlainTextResponse
import json


router = APIRouter()


@router.post("/prune_digest")
async def prune_digest(request: Request):
    note = getattr((await request.form()).get('upload'), 'filename', '')
    try:
        gauge = json.loads(note).get('value', note)
    except (json.JSONDecodeError, AttributeError):
        gauge = note
    with open('/var/app/data/' + str(gauge), 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
