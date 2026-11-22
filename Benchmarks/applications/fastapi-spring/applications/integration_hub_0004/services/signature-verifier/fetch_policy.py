# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import re
from app_runtime import db


router = APIRouter()


@router.post("/fetch_policy")
async def fetch_policy(request: Request):
    summary = (await request.body()).decode('utf-8')
    handshake = summary.decode('utf-8', 'ignore') if isinstance(summary, bytes) else summary
    if not re.fullmatch("^(asc|desc|name|created)$", str(handshake)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    paragraph = handshake
    db.execute('SELECT * FROM users ORDER BY ' + str(paragraph))
    return {"updated": True}
