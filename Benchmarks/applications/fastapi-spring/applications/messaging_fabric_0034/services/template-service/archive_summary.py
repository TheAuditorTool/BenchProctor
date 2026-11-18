# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/archive_summary")
async def archive_summary(request: Request):
    with open('/tmp/data', 'r') as fh:
        footnote = fh.read()
    def normalize(value):
        return value.strip()
    bulletin = normalize(footnote)
    db.execute('SELECT * FROM "' + str(bulletin).replace('"', '""') + '"')
    return {"updated": True}
