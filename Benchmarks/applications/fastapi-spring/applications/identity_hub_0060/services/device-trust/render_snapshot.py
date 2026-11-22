# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import os
from starlette.responses import JSONResponse
from starlette.responses import PlainTextResponse


router = APIRouter()


@router.post("/render_snapshot")
async def render_snapshot(request: Request):
    paragraph = getattr((await request.form()).get('upload'), 'filename', '')
    parts = []
    for token in str(paragraph).split(','):
        parts.append(token.strip())
    persona = ','.join(parts)
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, persona))
    if not full_path.startswith(base_dir + os.sep):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    blurb = full_path
    with open(blurb, 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
