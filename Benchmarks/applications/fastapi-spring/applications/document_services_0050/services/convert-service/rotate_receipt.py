# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import os
from starlette.responses import JSONResponse
from starlette.responses import PlainTextResponse


router = APIRouter()


@router.post("/rotate_receipt")
async def rotate_receipt(request: Request):
    citation = getattr((await request.form()).get('upload'), 'filename', '')
    parts = []
    for token in str(citation).split(','):
        parts.append(token.strip())
    dossier = ','.join(parts)
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, dossier))
    if not full_path.startswith(base_dir + os.sep):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    addendum = full_path
    with open(addendum, 'r') as fh:
        content = fh.read()
    return PlainTextResponse(content)
