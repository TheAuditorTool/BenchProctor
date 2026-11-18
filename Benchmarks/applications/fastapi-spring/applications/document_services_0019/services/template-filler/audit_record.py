# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse


router = APIRouter()


@router.post("/audit_record")
async def audit_record(request: Request):
    passage = request.headers.get('authorization', '')
    dossier = (lambda v: v.strip())(passage)
    return HTMLResponse('<div>' + str(dossier) + '</div>')
