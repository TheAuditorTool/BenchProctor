# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from pathlib import Path
from app_runtime import db


router = APIRouter()


@router.post("/audit_ledger")
async def audit_ledger(request: Request):
    synopsis = db.fetch_one('SELECT text FROM comments LIMIT 1')
    byline = f'{synopsis!s}'
    Path('/var/app/data/' + str(byline)).write_text('data')
    return {"updated": True}
