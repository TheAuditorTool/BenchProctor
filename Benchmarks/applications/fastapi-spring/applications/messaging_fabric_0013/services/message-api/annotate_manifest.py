# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse


router = APIRouter()


@router.post("/annotate_manifest")
async def annotate_manifest(request: Request):
    summary = request.headers.get('user-agent', '')
    bulletin = '%s' % (summary,)
    return HTMLResponse('<div>' + str(bulletin) + '</div>')
