# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/reconcile_config")
async def reconcile_config(request: Request):
    with open('/tmp/data', 'r') as fh:
        paragraph = fh.read()
    def normalize(value):
        return value.strip()
    persona = normalize(paragraph)
    db.execute('SELECT * FROM "' + str(persona).replace('"', '""') + '"')
    return {"updated": True}
