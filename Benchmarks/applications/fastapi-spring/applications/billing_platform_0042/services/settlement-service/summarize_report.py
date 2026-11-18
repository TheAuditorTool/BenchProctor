# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/summarize_report")
async def summarize_report(request: Request):
    with open('/tmp/data', 'r') as fh:
        remark = fh.read()
    def normalize(value):
        return value.strip()
    remittance = normalize(remark)
    db.execute('SELECT * FROM "' + str(remittance).replace('"', '""') + '"')
    return {"updated": True}
