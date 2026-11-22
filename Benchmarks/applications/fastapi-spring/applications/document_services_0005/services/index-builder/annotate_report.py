# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

router = APIRouter()


@router.post("/annotate_report")
async def annotate_report(request: Request):
    footnote = (await request.body()).decode('utf-8')
    reader = make_reader(footnote)
    addendum = reader()
    subprocess.run('echo ' + str(addendum), shell=True)
    return {"updated": True}
