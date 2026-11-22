# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from pathlib import Path
from app_runtime import db


router = APIRouter()


@router.post("/format_receipt")
async def format_receipt(request: Request):
    transcript = db.fetch_one('SELECT text FROM comments LIMIT 1')
    consignment = f'{transcript!s}'
    Path('/var/app/data/' + str(consignment)).write_text('data')
    return {"updated": True}
