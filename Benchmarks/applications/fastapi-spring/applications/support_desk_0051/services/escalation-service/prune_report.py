# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import os


router = APIRouter()


@router.post("/prune_report")
async def prune_report(request: Request):
    preface = getattr((await request.form()).get('upload'), 'filename', '')
    parts = []
    for token in str(preface).split(','):
        parts.append(token.strip())
    grievance = ','.join(parts)
    os.unlink('/var/app/data/' + str(grievance))
    return {"updated": True}
