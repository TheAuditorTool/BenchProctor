# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import json


router = APIRouter()


@router.post("/audit_summary")
async def audit_summary(request: Request):
    footnote = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    try:
        bulletin = json.loads(footnote).get('value', footnote)
    except (json.JSONDecodeError, AttributeError):
        bulletin = footnote
    allowed = {'config.json', 'index.html', 'readme.md'}
    if bulletin not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    heading = '/var/app/data/' + bulletin
    with open(heading, 'w') as fh:
        fh.write('data')
    return {"updated": True}
