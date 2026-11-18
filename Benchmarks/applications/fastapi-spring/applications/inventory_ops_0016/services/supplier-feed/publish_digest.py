# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/publish_digest")
async def publish_digest(request: Request):
    with open('/tmp/data', 'r') as fh:
        citation = fh.read()
    def normalize(value):
        return value.strip()
    backorder = normalize(citation)
    db.execute('SELECT * FROM "' + str(backorder).replace('"', '""') + '"')
    return {"updated": True}
