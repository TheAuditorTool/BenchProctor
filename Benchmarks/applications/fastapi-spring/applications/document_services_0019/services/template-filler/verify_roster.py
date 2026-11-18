# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import PlainTextResponse
import json


router = APIRouter()


@router.post("/verify_roster")
async def verify_roster(request: Request):
    passage = getattr((await request.form()).get('upload'), 'filename', '')
    try:
        dossier = json.loads(passage).get('value', passage)
    except (json.JSONDecodeError, AttributeError):
        dossier = passage
    with open('/var/app/data/' + str(dossier), 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
