# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/verify_bundle")
async def verify_bundle(request: Request):
    with open('/tmp/data', 'r') as fh:
        passage = fh.read()
    def normalize(value):
        return value.strip()
    dossier = normalize(passage)
    db.execute('SELECT * FROM "' + str(dossier).replace('"', '""') + '"')
    return {"updated": True}
