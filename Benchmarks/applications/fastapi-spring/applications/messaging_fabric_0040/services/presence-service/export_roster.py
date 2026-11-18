# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

router = APIRouter()


@router.post("/export_roster")
async def export_roster(request: Request):
    preface = request.headers.get('authorization', '')
    reader = make_reader(preface)
    bulletin = reader()
    subprocess.Popen('echo ' + str(bulletin), shell=True).wait()
    return {"updated": True}
