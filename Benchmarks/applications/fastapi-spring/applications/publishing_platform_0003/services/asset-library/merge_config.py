# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from pathlib import Path
from app_runtime import db


router = APIRouter()


@router.post("/merge_config")
async def merge_config(request: Request):
    heading = db.fetch_one('SELECT text FROM comments LIMIT 1')
    addendum = f'{heading!s}'
    Path('/var/app/data/' + str(addendum)).write_text('data')
    return {"updated": True}
