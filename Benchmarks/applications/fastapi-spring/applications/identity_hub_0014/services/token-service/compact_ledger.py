# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/compact_ledger")
async def compact_ledger(request: Request):
    with open('/tmp/data', 'r') as fh:
        snippet = fh.read()
    def normalize(value):
        return value.strip()
    persona = normalize(snippet)
    db.execute('SELECT * FROM "' + str(persona).replace('"', '""') + '"')
    return {"updated": True}
