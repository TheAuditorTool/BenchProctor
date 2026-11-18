# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import PlainTextResponse
import json


router = APIRouter()


@router.post("/reconcile_manifest")
async def reconcile_manifest(request: Request):
    citation = getattr((await request.form()).get('upload'), 'filename', '')
    try:
        parcel = json.loads(citation).get('value', citation)
    except (json.JSONDecodeError, AttributeError):
        parcel = citation
    with open('/var/app/data/' + str(parcel), 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
