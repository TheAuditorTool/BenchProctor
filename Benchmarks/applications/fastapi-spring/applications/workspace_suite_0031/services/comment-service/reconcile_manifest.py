# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import os


router = APIRouter()


@router.post("/reconcile_manifest")
async def reconcile_manifest(request: Request):
    caption = getattr((await request.form()).get('upload'), 'filename', '')
    parts = []
    for token in str(caption).split(','):
        parts.append(token.strip())
    synopsis = ','.join(parts)
    os.unlink('/var/app/data/' + str(synopsis))
    return {"updated": True}
