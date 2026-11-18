# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/enrich_receipt")
async def enrich_receipt(request: Request):
    with open('/tmp/data', 'r') as fh:
        notice = fh.read()
    def normalize(value):
        return value.strip()
    rendition = normalize(notice)
    db.execute('SELECT * FROM "' + str(rendition).replace('"', '""') + '"')
    return {"updated": True}
