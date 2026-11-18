# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import PlainTextResponse
import json


router = APIRouter()


@router.post("/build_policy")
async def build_policy(request: Request):
    footnote = getattr((await request.form()).get('upload'), 'filename', '')
    try:
        wording = json.loads(footnote).get('value', footnote)
    except (json.JSONDecodeError, AttributeError):
        wording = footnote
    with open('/var/app/data/' + str(wording), 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
