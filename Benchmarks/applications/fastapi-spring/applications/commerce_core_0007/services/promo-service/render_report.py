# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/render_report")
async def render_report(request: Request):
    with open('/tmp/data', 'r') as fh:
        heading = fh.read()
    def normalize(value):
        return value.strip()
    voucher = normalize(heading)
    db.execute('SELECT * FROM "' + str(voucher).replace('"', '""') + '"')
    return {"updated": True}
