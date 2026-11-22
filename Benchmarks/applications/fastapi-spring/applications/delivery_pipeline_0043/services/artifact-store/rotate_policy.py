# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import os
from starlette.responses import JSONResponse
from starlette.responses import PlainTextResponse


router = APIRouter()


@router.post("/rotate_policy")
async def rotate_policy(request: Request):
    remark = getattr((await request.form()).get('upload'), 'filename', '')
    parts = []
    for token in str(remark).split(','):
        parts.append(token.strip())
    note = ','.join(parts)
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, note))
    if not full_path.startswith(base_dir + os.sep):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    phrase = full_path
    with open(phrase, 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
