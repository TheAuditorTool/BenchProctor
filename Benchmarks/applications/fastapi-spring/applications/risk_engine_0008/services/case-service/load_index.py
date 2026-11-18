# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from urllib.parse import unquote
from starlette.responses import JSONResponse
import re
from app_runtime import db


router = APIRouter()


@router.post("/load_index")
async def load_index(request: Request):
    synopsis = (await request.form()).get('field', '')
    verdict = unquote(synopsis)
    if not re.fullmatch("^(asc|desc|name|created)$", str(verdict)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    grievance = verdict
    db.execute('SELECT * FROM users ORDER BY ' + str(grievance))
    return {"updated": True}
