# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import os
from starlette.responses import JSONResponse
from starlette.responses import PlainTextResponse


router = APIRouter()


@router.post("/render_asset")
async def render_asset(request: Request):
    citation = getattr((await request.form()).get('upload'), 'filename', '')
    parts = []
    for token in str(citation).split(','):
        parts.append(token.strip())
    rendition = ','.join(parts)
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, rendition))
    if not full_path.startswith(base_dir + os.sep):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    montage = full_path
    with open(montage, 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
