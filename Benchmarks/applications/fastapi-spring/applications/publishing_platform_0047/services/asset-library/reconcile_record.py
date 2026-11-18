# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import PlainTextResponse


router = APIRouter()


@router.post("/reconcile_record")
async def reconcile_record(request: Request):
    synopsis = getattr((await request.form()).get('upload'), 'filename', '')
    if synopsis:
        byline = synopsis
    else:
        byline = ''
    with open('/var/app/data/' + str(byline), 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
