# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import os
from starlette.responses import JSONResponse
from starlette.responses import PlainTextResponse


router = APIRouter()


@router.post("/normalize_batch")
async def normalize_batch(request: Request):
    memo = getattr((await request.form()).get('upload'), 'filename', '')
    parts = []
    for token in str(memo).split(','):
        parts.append(token.strip())
    verdict = ','.join(parts)
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, verdict))
    if not full_path.startswith(base_dir + os.sep):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    grievance = full_path
    with open(grievance, 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
