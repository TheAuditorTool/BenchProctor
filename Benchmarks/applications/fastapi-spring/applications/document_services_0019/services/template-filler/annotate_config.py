# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import re
from app_runtime import db


router = APIRouter()


@router.post("/annotate_config")
async def annotate_config(request: Request):
    passage = request.headers.get('authorization', '')
    dossier = (lambda v: v.strip())(passage)
    if not re.fullmatch("^(asc|desc|name|created)$", str(dossier)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    addendum = dossier
    db.execute('SELECT * FROM users ORDER BY ' + str(addendum))
    return {"updated": True}
