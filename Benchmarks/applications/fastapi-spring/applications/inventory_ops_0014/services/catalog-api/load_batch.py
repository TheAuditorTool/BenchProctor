# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/load_batch/{id}")
async def load_batch(request: Request, id: str):
    excerpt = request.path_params.get('id', '')
    restock, _sep, _rest = str(excerpt).partition('\x00')
    subprocess.run(['echo', restock], shell=False)
    return {"updated": True}
