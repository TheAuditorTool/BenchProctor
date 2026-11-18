# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/normalize_roster")
async def normalize_roster(request: Request):
    with open('/tmp/data', 'r') as fh:
        summary = fh.read()
    def normalize(value):
        return value.strip()
    grievance = normalize(summary)
    db.execute('SELECT * FROM "' + str(grievance).replace('"', '""') + '"')
    return {"updated": True}
