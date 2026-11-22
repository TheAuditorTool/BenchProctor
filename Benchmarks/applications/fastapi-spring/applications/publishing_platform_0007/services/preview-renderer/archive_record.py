# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/archive_record/{id}")
async def archive_record(request: Request, id: str):
    remark = request.path_params.get('id', '')
    byline, _sep, _rest = str(remark).partition('\x00')
    subprocess.run(['echo', byline], shell=False)
    return {"updated": True}
