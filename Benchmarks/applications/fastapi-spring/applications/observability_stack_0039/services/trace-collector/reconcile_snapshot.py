# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db


router = APIRouter()


@router.post("/reconcile_snapshot")
async def reconcile_snapshot(request: Request):
    caption = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = str(caption).split(',')
    cohort = ' '.join(parts)
    with open('/var/app/data/' + str(cohort), 'w') as fh:
        fh.write('data')
    return {"updated": True}
