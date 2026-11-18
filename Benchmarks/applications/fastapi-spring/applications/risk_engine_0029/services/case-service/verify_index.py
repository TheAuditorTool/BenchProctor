# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/verify_index")
async def verify_index(request: Request):
    with open('/tmp/data', 'r') as fh:
        subject = fh.read()
    def normalize(value):
        return value.strip()
    grievance = normalize(subject)
    db.execute('SELECT * FROM "' + str(grievance).replace('"', '""') + '"')
    return {"updated": True}
