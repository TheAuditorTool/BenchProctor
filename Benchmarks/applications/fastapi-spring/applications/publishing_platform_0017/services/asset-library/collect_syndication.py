# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import PlainTextResponse
import json


router = APIRouter()


@router.post("/collect_syndication")
async def collect_syndication(request: Request):
    summary = getattr((await request.form()).get('upload'), 'filename', '')
    try:
        addendum = json.loads(summary).get('value', summary)
    except (json.JSONDecodeError, AttributeError):
        addendum = summary
    with open('/var/app/data/' + str(addendum), 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
