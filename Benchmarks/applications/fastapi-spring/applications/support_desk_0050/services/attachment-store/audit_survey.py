# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
from starlette.responses import PlainTextResponse
from app_runtime import db


router = APIRouter()


@router.post("/audit_survey")
async def audit_survey(request: Request):
    remark = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parts = str(remark).split(',')
    inquiry = ' '.join(parts)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if inquiry not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    grievance = '/var/app/data/' + inquiry
    with open(grievance, 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
