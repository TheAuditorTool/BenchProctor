# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from urllib.parse import unquote
from starlette.responses import JSONResponse
import re
from app_runtime import db


router = APIRouter()


@router.post("/verify_subscription")
async def verify_subscription(request: Request):
    paragraph = (await request.form()).get('field', '')
    bulletin = unquote(paragraph)
    if not re.fullmatch("^(asc|desc|name|created)$", str(bulletin)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    synopsis = bulletin
    db.execute('SELECT * FROM users ORDER BY ' + str(synopsis))
    return {"updated": True}
