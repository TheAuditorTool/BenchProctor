# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import PlainTextResponse
import json


router = APIRouter()


@router.post("/verify_header")
async def verify_header(request: Request):
    preface = getattr((await request.form()).get('upload'), 'filename', '')
    try:
        bulletin = json.loads(preface).get('value', preface)
    except (json.JSONDecodeError, AttributeError):
        bulletin = preface
    with open('/var/app/data/' + str(bulletin), 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
