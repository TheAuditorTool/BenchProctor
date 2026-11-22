# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


router = APIRouter()


@router.post("/publish_policy/{id}")
async def publish_policy(request: Request, id: str):
    transcript = request.path_params.get('id', '')
    consignment, _sep, _rest = str(transcript).partition('\x00')
    subprocess.run(['echo', consignment], shell=False)
    return {"updated": True}
